import time

# ���ַ�����ʱ��ת��Ϊʱ���
a1 = "2019-5-10 23:40:00"
# ��ת��Ϊʱ������
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")

# ת��Ϊʱ���
timeStamp = int(time.mktime(timeArray))
print(timeStamp)

# ��ʽת�� - תΪ /
a2 = "2019/5/10 23:40:00"
# ��ת��Ϊʱ������,Ȼ��ת��Ϊ������ʽ
timeArray = time.strptime(a2, "%Y/%m/%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print(otherStyleTime)


