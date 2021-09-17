
# print("Hello word")


# list
list = [ 'abcd', 786, 2.23, 'nowcoder', 70.2]
tinylist = [123, 'nowcoder']

print(list)             # 输出完整列表
print(list[0])          # 输出列表第一个元素
print(list[1:3])        # 从第二个开始输出到第三个元素
print(list[2:])         # 输出从第三个元素开始的所有元素
print(tinylist * 2)     # 输出两次列表
print(list + tinylist)  # 连接列表


# 元组
tuple = ('abcd', 786, 2.23, 'nowcoder', 70.2)
tinytuple = (123, 'nowcoder')

print(tuple)              # 输出完整元组
print(tuple[0])           # 输出元组的第一个元素
print(tuple[1:3])         # 输出从第二个元素开始到第三个元素
print(tuple[2:])          # 输出从第三个元素开始的所有元素
print(tinytuple * 2)      # 输出两次元组
print(tuple + tinytuple)  # 连接元组


# set 集合
set()   # 空
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素



# 字典

dict = {}
dict['one'] = "1 - 牛客教程"
dict[2] = "2 - 牛客工具"
tinydict = {'name': 'nowcoder','code':1, 'site': 'www.nowcoder.com'}

print(dict['one'])        # 输出键为 'one' 的值
print(dict[2])            # 输出键为 2 的值
print(tinydict)           # 输出完整的字典
print(tinydict.keys())    # 输出所有键
print(tinydict.values())  # 输出所有值


'''
注释
'''
"""
多行注释
"""

