# -*- coding: utf-8 -*-
import json
import time

import SparkApiTest

data_set_path = "C:\\Users\\gumo\\Desktop\\apiTestDoc(include datasets)\\datasets\\"
target_path = "C:\\Users\\gumo\\Desktop\\apiTestDoc(include datasets)\\xfyunPython\\"
file_name = "ceval.json"

input_path = data_set_path + file_name
output_path = target_path + file_name

def fetch_answer(question):
    try:
        # 调用讯飞接口
        prefix = "你是一个答题助手,可以专业的简洁的输出问题的答案,请阅读下面选择题,简洁的输出正确选项前的字母不需要输出答案和多余的字符: ";
        answer = SparkApiTest.get_answer(prefix + question)
        if "AppIdQpsOverFlowError" in answer:
            time.sleep(0.5)
            answer = fetch_answer(question)

        print("### 返回结果:  " + answer.encode('utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
    except Exception as e:
        answer = fetch_answer(question)
        print(e)
    return answer

def build_output_json_node(input_json_data):
    output_json_data = {
        "api_name": "testXunFeiYun",
        "concurrency": True,
        "params": {
            "max_length": 767,
            "num_beams": 1,
            "do_sample": True,
            "top_p": 0.9,
            "temperature": 0.95,
            "max_gen_length": 256
        },
        "answers": []
    }

    for input_element in input_json_data:
        answer_element = {
            "id": input_element["id"],
            "q": input_element["q"],
            "gt": input_element["gt"]
        }

        print(input_element)
        answer = fetch_answer(input_element["q"])
        answer_element["answer"] = answer
        output_json_data["answers"].append(answer_element)

    return output_json_data

def upload_json():
    try:
        with open(input_path, "r", encoding="utf-8") as input_file:
            input_json_data = json.load(input_file)

        output_json_data = build_output_json_node(input_json_data)

        with open(output_path, "w", encoding='utf-8') as output_file:
            json.dump(output_json_data, output_file, indent=4)

        print("JSON 文件已成功读取、修改并写入。")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # 测试时候在此处正确填写相关信息即可运行
    upload_json()

