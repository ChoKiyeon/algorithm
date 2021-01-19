finding_target = 11
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    low = 0
    high = len(array) - 1
    middle = (low + high) // 2

    while array[middle] is not target:
        if low >= high:
            return False

        if array[middle] > target:
            high = middle - 1
        else:
            low = middle + 1

        middle = (low + high) // 2

    return True


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
