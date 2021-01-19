array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    # 이 부분을 채워보세요!
    array_c = []
    a_index = 0
    b_index = 0

    while a_index != len(array_a) and b_index != len(array_b):
        if array_a[a_index] > array_b[b_index]:
            array_c.append(array_b[b_index])
            b_index += 1
        else:
            array_c.append(array_a[a_index])
            a_index += 1

    if a_index == len(array_a):
        for i in range(b_index, len(array_b)):
            array_c.append(array_b[i])
    else:
        for i in range(a_index, len(array_a)):
            array_c.append(array_a[i])

    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!