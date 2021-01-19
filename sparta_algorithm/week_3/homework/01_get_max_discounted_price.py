shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    prices_count = 0
    price = 0

    for index in range(len(coupons)):
        price += prices[index] * (1 - (coupons[index] / 100))
        prices_count += 1

    while prices_count != len(prices):
        price += prices[prices_count]
        prices_count += 1
    return price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
