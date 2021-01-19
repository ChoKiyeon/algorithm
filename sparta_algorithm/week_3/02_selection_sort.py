input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    min_index = 0

    for i in range(len(array) - 1):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
