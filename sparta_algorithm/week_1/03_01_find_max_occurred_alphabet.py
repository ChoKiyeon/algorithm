input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26
    count = 97

    for char in string:
        if char.isalpha():
            alphabet_occurrence_array[(ord(char) - ord('a'))] += 1

    for num in alphabet_occurrence_array:
        for compare_num in alphabet_occurrence_array:
            if num < compare_num:
                break
        else:
            return chr(count)
        count += 1


result = find_max_occurred_alphabet(input)
print(result)
