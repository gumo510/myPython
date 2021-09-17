

thisset = set(("Google", "Nowcoder", "Taobao"))

#  添加集合
thisset.add("Facebook")
print(thisset)

# 添加元素 参数可以是列表，元组，字典等
thisset.update([1, 2])
print(thisset)

# 移除元素 不存在报错
thisset.remove(1)
print(thisset)
# 移除元素 不存在不会报错
thisset.discard(3)
print(thisset)

# 随机删除元素
thisset.pop()
print(thisset)

len = len(thisset)
thisset.clear()
var = 1 in thisset

