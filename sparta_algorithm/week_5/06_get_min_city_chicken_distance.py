import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    chicken_location = []
    home_location = []

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location.append((i + 1, j + 1))
            elif city_map[i][j] == 2:
                chicken_location.append((i + 1, j + 1))

    for r, c in chicken_location:
        print(r, c)
    return


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!