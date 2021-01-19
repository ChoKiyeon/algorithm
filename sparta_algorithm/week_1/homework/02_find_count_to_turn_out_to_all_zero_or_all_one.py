input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    count_zero = 0
    count_one = 0

    if string[0] == '1':
        count_zero += 1
    else:
        count_one += 1

    for index in range(len(string) - 1):
        if string[index] != string[index + 1]:
            if string[index + 1] == '1':
                count_zero += 1
            else:
                count_one += 1

    return min(count_zero, count_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)