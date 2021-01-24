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


def absolute_value_add(num_1, num_2):
    if num_1 < 0:
        num_1 = -num_1
    if num_2 < 0:
        num_2 = -num_2

    return num_1 + num_2


def get_min_city_chicken_distance(n, m, city_map):
    chicken_location = []
    home_location = []
    chicken_distance = []

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location.append([i + 1, j + 1])
            elif city_map[i][j] == 2:
                chicken_location.append([i + 1, j + 1])

    chicken_location_m_combinations = list(itertools.combinations(chicken_location, m))
    min_distance_of_m_combinations = sys.maxsize

    for chicken_location_m_combination in chicken_location_m_combinations:
        city_chicken_distance = 0
        for home_r, home_c in home_location:
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_m_combination:  #
                min_home_chicken_distance = min(    # 제일 작은 치킨 거리 기록
                    min_home_chicken_distance, abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )
            city_chicken_distance += min_home_chicken_distance  # 도시 치킨 거리에 집에서 가장 가까운 치킨 거리 더하기
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, city_chicken_distance) # 제일 작은 치킨 거리의 합을 기록
    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
