def find_alphabet_occurrence_array(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha():
            alphabet_occurrence_array[(ord(char) - ord('a'))] += 1
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
