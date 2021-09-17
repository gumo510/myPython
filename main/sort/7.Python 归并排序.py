def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # ������ʱ����
    L = [0] * (n1)
    R = [0] * (n2)

    # �������ݵ���ʱ���� arrays L[] �� R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # �鲢��ʱ���鵽 arr[l..r]
    i = 0  # ��ʼ����һ�������������
    j = 0  # ��ʼ���ڶ��������������
    k = l  # ��ʼ�鲢�����������

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # ���� L[] �ı���Ԫ��
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # ���� R[] �ı���Ԫ��
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = int((l + (r - 1)) / 2)

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("����������")
for i in range(n):
    print("%d" % arr[i]),

mergeSort(arr, 0, n - 1)
print("\n\n����������")
for i in range(n):
    print("%d" % arr[i]),
