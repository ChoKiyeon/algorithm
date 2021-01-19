current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
direction = [0, 3, 2, 1]


# 방향 전환
def direction_left_turn(left):
    d = left.pop(0)
    left.append(d)
    return left[0]


# 후진
def back(d):
    if d == 0:
        return 2
    elif d == 3:
        return 1
    elif d == 2:
        return 0
    else:
        return 3


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    x = len(room_map)
    y = len(room_map[0])
    count_cleaned_room = 1
    room_map[r][c] = 2
    queue = list([[r, c, d]])

    # 큐가 비어지면 종료
    while True:
        r, c, d = queue.pop(0)
        temp_d = d

        for i in range(len(direction)):
            temp_d = direction_left_turn(direction)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= new_r < x and 0 <= new_c < y and room_map[new_r][new_c] == 0:
                count_cleaned_room += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break

        else:   # 4방향 모두 청소할 곳이 없을 경우
            new_r, new_c = r + dr[back(d)], c + dc[back(d)]
            queue.append([new_r, new_c, d])

            if room_map[new_r][new_c] == 1:
                return count_cleaned_room


print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
