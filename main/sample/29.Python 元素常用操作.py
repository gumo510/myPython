# ����Ԫ�����б��г��ֵĴ���
def countX(lst, x):
    return lst.count(x)


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))

# �����б�Ԫ��֮��
list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("�б�Ԫ��֮��Ϊ: ", total)

# �����б�����СԪ��
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("��СԪ��Ϊ:", *list1[:1])
list1 = [10, 20, 1, 45, 99]
print("��СԪ��Ϊ:", min(list1))

# �����б������Ԫ��
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("���Ԫ��Ϊ:", list1[-1])
list1 = [10, 20, 1, 45, 99]
print("���Ԫ��Ϊ:", max(list1))
