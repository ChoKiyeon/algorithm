import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    heap = []
    date = 0
    count = 0

    while stock < k:
        for index in range(date, len(dates)):
            if stock >= dates[index]:   # 재고에 여유가 남으면 힙에 공급 가능한 수량을 저장
                heapq.heappush(heap, -supplies[index])
            else:
                date = index  # 재고에 여유가 남지 않으면 재고 공급 후 이미 공급한 날짜는 넘김
                break

        count += 1  # 공급 횟수 + 1
        stock += -heapq.heappop(heap)   # 제일 많이 받아올 수 있는 재고 공급

    return count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
