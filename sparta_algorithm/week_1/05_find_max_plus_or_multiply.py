input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    sum = array[0]
    for index in range(len(array) - 1):
        if (sum + array[index + 1]) < (sum * array[index + 1]):
            sum *= array[index + 1]
        else:
            sum += array[index + 1]
    return sum


result = find_max_plus_or_multiply(input)
print(result)