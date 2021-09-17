# 计算元素在列表中出现的次数
def countX(lst, x):
    return lst.count(x)


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))

# 计算列表元素之和
list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("列表元素之和为: ", total)

# 查找列表中最小元素
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("最小元素为:", *list1[:1])
list1 = [10, 20, 1, 45, 99]
print("最小元素为:", min(list1))

# 查找列表中最大元素
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("最大元素为:", list1[-1])
list1 = [10, 20, 1, 45, 99]
print("最大元素为:", max(list1))
