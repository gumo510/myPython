
"""
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
"""


"""
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
"""


languages = ["C", "C++", "Perl", "Python"]
for lang in languages:
    print(lang)

# 遍历数字
# for i in range(5, 9):
#     print(i)

for i in range(0, 10, 2):
    print(i)

# 生成数组
print(list(range(5)))


# 迭代器 iter() 和 next()。
print("# 迭代器 iter() 和 next()。")
lists = [1, 2, 3, 4]
it = iter(lists)
# print(next(it))
# print(next(it))
for x in it:
    print(x)


print("输出")
lists = "Hello, Nowcoder"
print(lists)
str(lists)
repr(lists)
