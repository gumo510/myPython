# ����ʵ��һ
print("����ʵ��һ")
str = "nowcoder.com"
print(str.isalnum())  # �ж������ַ��������ֻ�����ĸ
print(str.isalpha())  # �ж������ַ�������ĸ
print(str.isdigit())  # �ж������ַ���������
print(str.islower())  # �ж������ַ�����Сд
print(str.isupper())  # �ж������ַ����Ǵ�д
print(str.istitle())  # �ж����е��ʶ�������ĸ��д�������
print(str.isspace())  # �ж������ַ����ǿհ��ַ���\t��\n��\r

print("------------------------")

# ����ʵ����
print("����ʵ����")
str = "nowcoder"
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str.isspace())

# �ַ�����Сдת��
str = "www.nowcoder.com"
print(str.upper())          # �������ַ��е�Сд��ĸת���ɴ�д��ĸ
print(str.lower())          # �������ַ��еĴ�д��ĸת����Сд��ĸ
print(str.capitalize())     # �ѵ�һ����ĸת��Ϊ��д��ĸ������Сд
print(str.title())          # ��ÿ�����ʵĵ�һ����ĸת��Ϊ��д������Сд