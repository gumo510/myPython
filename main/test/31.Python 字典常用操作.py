# �����ֵ�ֵ֮��
data = {'a': 100, 'b': 200, 'c': 300}
num = sum(data.values())
print(num)

#
test_dict = {"Nowcoder": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

# ���ԭʼ���ֵ�
print("�ֵ��Ƴ�ǰ : " + str(test_dict))

# ʹ�� del �Ƴ� Zhihu
del test_dict['Zhihu']

# ����Ƴ�����ֵ�
print("�ֵ��Ƴ��� : " + str(test_dict))

# �Ƴ�û�е� key �ᱨ��
# del test_dict['Baidu']
