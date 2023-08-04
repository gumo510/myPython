import backoff, openai, tiktoken, time, logging.handlers, sys, json, re, os
from concurrent.futures import ThreadPoolExecutor, wait
from multiprocessing import JoinableQueue
from pydantic import BaseModel

logger = logging.getLogger()
logger.setLevel(logging.INFO)
rht = logging.handlers.TimedRotatingFileHandler("qa.log", 'D', encoding='utf-8')
fmt = logging.Formatter("%(asctime)s %(pathname)s %(filename)s %(funcName)s %(lineno)s \
      %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
rht.setFormatter(fmt)
logger.addHandler(rht)
sh = logging.StreamHandler(stream=sys.stdout)  # output to standard output
sh.setFormatter(fmt)
logger.addHandler(sh)
queue = JoinableQueue(2000)


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


def get_encoder(model):
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo" or model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif model == "gpt-3.5-turbo-16k":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif model == "gpt-4-0314" or model == "gpt-4-0613":
        tokens_per_message = 3
        tokens_per_name = 1
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai
            -python/blob/main/chatml.md for information on how messages are converted to tokens.""")
    return encoding, tokens_per_message, tokens_per_name


class ChatGPT:
    def __init__(self, api_key, model):
        openai.api_key = api_key
        self.model = model
        self.system_dict = {"role": "system", "content": "你是一个答题助手,可以专业的简洁的输出问题的答案,请阅读下面选择题,简洁的输出正确选项前的字母不需要输出答案和多余的字符"}

        self.encoding, self.tokens_per_message, self.tokens_per_name = get_encoder(model)

    def chat(self, tokenizer, chat_query, history, max_length=4096, temperature=0.01):
        message_rev = [{"role": "user", "content": chat_query}]

        num_tokens = self.tokens_per_message  # count current query
        for key, value in message_rev[0].items():
            num_tokens += len(self.encoding.encode(value))

        num_tokens += self.tokens_per_message  # count system
        for key, value in self.system_dict.items():
            num_tokens += len(self.encoding.encode(value))

        for query, response in history[-4::][::-1]:  # 最多取最近4轮问答
            message_tmp = [{"role": "assistant", "content": response}, {"role": "user", "content": query}]
            for msg in message_tmp:
                num_tokens += self.tokens_per_message  # count system
                for key, value in msg.items():
                    num_tokens += len(self.encoding.encode(value))
            if num_tokens <= max_length:  # 太长了就不要放太多历史记录了
                message_rev.extend(message_tmp)
            else:
                break
        num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        message_rev.append(self.system_dict)
        message = message_rev[::-1]
        # print(f"message len {num_tokens} to chatgpt: {message}")

        start_time = time.time()
        response = completions_with_backoff(
            model=self.model,
            messages=message,
            temperature=temperature
        )
        final_response = response['choices'][0]['message']['content']
        prompt_tokens = response['usage']['prompt_tokens']
        total_tokens = response['usage']['total_tokens']
        logger.info(
            f"ChatGPT prompt tokens {prompt_tokens} total tokens {total_tokens}, estimated tokens {num_tokens}, "
            f"response time {time.time() - start_time:.3f}")
        return final_response, history


class Param(BaseModel):
    max_length: int = 4096
    num_beams: int = 1
    do_sample: bool = True
    top_p: float = 1.0
    temperature: float = 0.01
    max_gen_length: int = 256


class Answer(BaseModel):
    id: int
    q: str
    gt: str
    answer: str = None

    def to_json(self):
        data = {
            'id': self.id,
            'q': self.q,
            'gt': self.gt,
            'answer': self.answer
        }
        return json.dumps(data, ensure_ascii=False)


class Result(BaseModel):
    api_name: str = "GPT-3.5"
    concurrency: bool = True
    params: dict = Param().__dict__
    answers: list = []


"""
可配置的参数
"""
# 并发数量
concurrent_quantity = 4
# 设置apikey
apikey = "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"
# 设置模型版本
model_version = "gpt-3.5-turbo-0301"
# 试题存放的位置
data_set_path = r"C:\Users\gumo\Desktop\apiTestDoc(include datasets)\datasets\webqa.json"
# 答案生成的位置
target_path = r"C:\Users\gumo\Desktop\apiTestDoc(include datasets)\result"


futures: list = []
tpe = ThreadPoolExecutor(concurrent_quantity, 'chat')
cur = os.path.dirname(os.path.abspath(__file__))
chat_boot = ChatGPT(api_key=apikey, model=model_version)
def parse_data(path):
    with open(path, mode='rt', encoding='utf-8') as file:
        return json.load(file)


def generate_answer(dic: dict, index: int):
    try:
        result, _ = chat_boot.chat(None, dic['q'], [])
        logger.info(f'已生成第{index+1}个问题')
        answer = Answer(id=dic['id'], q=dic['q'], gt=dic['gt'])
        answer.answer = result
        queue.put(answer.__dict__)
    except Exception as e:
        # 失败的写入文件
        fail_path = os.path.join(cur, 'fail.json')
        with open(fail_path, 'at', encoding='utf-8') as fail:
            json.dump(dic, fail, ensure_ascii=False)
            fail.write("\n")
        logger.error(f'write_answer: {e}')


# 定义消费者函数
def consumer():
    logger.info('消费者启动...')
    try:
        tmp_path = os.path.join(cur, 'tmp.json')
        with open(tmp_path, 'at', encoding='utf-8') as f:
            while True:
                task = queue.get()
                if isinstance(task, str) and str(task).__eq__('[DONE]'):
                    break
                json.dump(task, f, ensure_ascii=False)
                f.write("\n")
    except Exception as e:
        logger.error(f'consumer: {e}')
    finally:
        logger.info('消费者关闭...')


def submit_task():
    tpe.submit(consumer)
    for index, dic in enumerate(parse_data(data_set_path)):
        logger.info(f'提交第{index + 1}个任务')
        futures.append(tpe.submit(generate_answer, dic, index))
    logger.info('任务提交结束')
    wait(futures, return_when='ALL_COMPLETED')
    queue.put('[DONE]')


def format_tmp_json():
    tmp_path = os.path.join(cur, 'tmp.json')
    try:
        jsons = []
        with open(tmp_path, 'rt', encoding='utf-8') as lines:
            for line in lines:
                jsons.append(json.loads(line))
        param = Param(max_length=4096, temperature=0.01)
        result = Result(api_name="GPT-3.5", params=param.__dict__, answers=jsons)
        with open(os.path.join(target_path, 'result.json'), 'wt', encoding='utf-8') as file:
            json.dump(result.__dict__, file, ensure_ascii=False, indent=2)
        os.remove(tmp_path)
    except Exception as e:
        logger.error("format_tmp_json", e)
    finally:
        if os.path.exists(tmp_path):
            os.rename(tmp_path, os.path.join(cur, 'tmp_bak.json'))


submit_task()
format_tmp_json()
tpe.shutdown(wait=True)

logger.info('----------------------- 任务执行完毕 -----------------------')
