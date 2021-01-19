shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()

    for index in range(len(orders)):
        low = 0
        high = len(menus) - 1
        middle = (low + high) // 2

        while menus[middle] is not orders[index]:
            if low > high:
                return False
            elif menus[middle] < orders[index]:
                low = middle + 1
            else:
                high = middle - 1

            middle = (low + high) // 2
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
