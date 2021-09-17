import re


# 移除字符串中的指定位置字符
def RemoveChar(test_str, position):
    list_str = list(test_str)
    list_str.pop(position - 1)
    return ''.join(list_str)


# 判断字符串是否存在子字符串
def RemoveChar(test_str, position):
    list_str = list(test_str)
    list_str.pop(position - 1)
    return ''.join(list_str)


# 判断字符串长度
str1 = "nowCoder"
print(len(str1))


# 使用正则表达式提取字符串中的 URL
def Find(string):
    # findall() 查找匹配正则表达式的字符串
    assert isinstance(string, object)
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url


string = 'Nowcoder 的网页地址为：https://www.nowcoder.com，Google 的网页地址为：https://www.google.com'
print("Urls: ", Find(string))

# 字符串翻转 或使用 reversed()
str1 = 'nowCoder'
print(str[::-1])
print(''.join(reversed(str)))
