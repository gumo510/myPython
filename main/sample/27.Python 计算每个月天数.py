import calendar
import datetime

monthRange = calendar.monthrange(2016, 9)
# �������һ��Ԫ�飬��һ��Ԫ���������·ݵĵ�һ���Ӧ�������ڼ���0-6����
# �ڶ���Ԫ��������µ�����������ʵ���������˼Ϊ 2016 �� 9 �·ݵĵ�һ���������ģ������ܹ��� 30 �졣
print(monthRange)


# ��ȡ��������
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


# ���
print(getYesterday())
