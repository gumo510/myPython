# ���� x �� arr �е���������������ڷ��� -1
def binarySearch(arr, l, r, x):
    # �����ж�
    if r >= l:

        mid = int(l + (r - l) / 2)

        # Ԫ�����õ��м�λ��
        if arr[mid] == x:
            return mid

        # Ԫ��С���м�λ�õ�Ԫ�أ�ֻ��Ҫ�ٱȽ���ߵ�Ԫ��
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Ԫ�ش����м�λ�õ�Ԫ�أ�ֻ��Ҫ�ٱȽ��ұߵ�Ԫ��
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # ������
        return -1


# ��������
arr = [2, 3, 4, 10, 40]
x = 10

# ��������
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Ԫ���������е�����Ϊ %d" % result)
else:
    print("Ԫ�ز���������")
