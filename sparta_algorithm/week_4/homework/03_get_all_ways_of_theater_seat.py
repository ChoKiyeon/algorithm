seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}


def fibo(n, fibo_memo):
    if n == 0:
        return 1
    if n in fibo_memo:
        return fibo_memo[n]

    plus_fibo = fibo(n - 1, fibo_memo) + fibo(n - 2, fibo_memo)
    fibo_memo[n] = plus_fibo

    return plus_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    start_index = [0]
    ways_of_seat = 1

    for index in range(len(fixed_seat_array) + 1):
        count = 0

        if index == len(fixed_seat_array):
            vip_seat = total_count + 1
        else:
            vip_seat = fixed_seat_array[index]

        for seat in range(start_index.pop() + 1, total_count + 1):
            if seat == vip_seat:
                start_index.append(seat)
                break
            count += 1

        ways_of_seat *= fibo(count, memo)
    return ways_of_seat


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
