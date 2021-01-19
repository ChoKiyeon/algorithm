finding_target = 7
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    # 이 부분을 채워보세요!
    for index in range(len(numbers)):
        if target == numbers[index]:
            return True
    else:
        return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)