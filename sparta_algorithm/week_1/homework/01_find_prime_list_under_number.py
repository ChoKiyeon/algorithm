input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime = []
    for num in range(2, input + 1):
        for remainder_num in prime:
            if num % remainder_num == 0 and remainder_num * remainder_num <= num:
                break
        else:
            prime.append(num)

    return prime


result = find_prime_list_under_number(input)
print(result)
