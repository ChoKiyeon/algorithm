array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    if len(array) <= 1:  # 탈출 조건
        return array

    mid_index = len(array) // 2  # 배열의 중간 인덱스

    left_array = merge_sort(array[:mid_index])   # 배열의 왼쪽 부분을 재귀
    right_array = merge_sort(array[mid_index:])  # 배열의 오른쪽 부분을 재귀
                                                 # 정렬된 값이 변수로 반환 됨
    return merge(left_array, right_array)  # merge -> 병합 정렬을 해주는 함수를 이용해 정렬


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
