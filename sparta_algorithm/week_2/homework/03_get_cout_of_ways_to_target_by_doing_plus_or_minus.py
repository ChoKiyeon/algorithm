numbers = [1, 1, 1, 1, 1]
target_number = 3
count_result = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, index, sum):
    global count_result

    if index == (len(numbers)):  # 함수가 배열의 길이만큼 재귀 했는지 체크
        if sum == target:      # 배열의 모든 원소를 더하거나 뺀 값이 구하려는 수(target)와 같다면
            count_result += 1  # count_result에 카운팅
        return

    # 위의 그림과 같이 모든 경우의 수로 재귀
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, index + 1, sum + array[index])  # 더하는 경우
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, index + 1, sum - array[index])  # 빼는 경우


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(count_result)
