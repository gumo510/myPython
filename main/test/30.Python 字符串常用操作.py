import re


# �Ƴ��ַ����е�ָ��λ���ַ�
def RemoveChar(test_str, position):
    list_str = list(test_str)
    list_str.pop(position - 1)
    return ''.join(list_str)


# �ж��ַ����Ƿ�������ַ���
def RemoveChar(test_str, position):
    list_str = list(test_str)
    list_str.pop(position - 1)
    return ''.join(list_str)


# �ж��ַ�������
str1 = "nowCoder"
print(len(str1))


# ʹ��������ʽ��ȡ�ַ����е� URL
def Find(string):
    # findall() ����ƥ��������ʽ���ַ���
    assert isinstance(string, object)
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url


string = 'Nowcoder ����ҳ��ַΪ��https://www.nowcoder.com��Google ����ҳ��ַΪ��https://www.google.com'
print("Urls: ", Find(string))

# �ַ�����ת ��ʹ�� reversed()
str1 = 'nowCoder'
print(str[::-1])
print(''.join(reversed(str)))
