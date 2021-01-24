from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
# 서, 북, 동, 남
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def move_until_wall_or_hole(r, c, diff_r, diff_c, map):  # 벽이 나올 때까지 이동하는 함수
    move_count = 0

    while map[r + diff_r][c + diff_c] != '#' and map[r][c] != 'O':  # 벽이거나 현재 위치가 구멍이 아닐경우 이동
        r += diff_r
        c += diff_c
        move_count += 1

    return r, c, move_count


def is_available_to_take_out_only_red_marble(map):  # 큐가 비었을 경우에는 전부 가봤던 곳이거나 블루가 전부 이겼으므로 게임이 끝나지 않는다.
    # 구현해보세요!
    n, m = len(map), len(map[0])  # 게임 맵의 가로, 세로 길이
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    red_row, red_col, blue_row, blue_col = 1, 1, 1, 1

    for i in range(n):  # 구슬의 초기 위치 받아오기
        for j in range(m):
            if map[i][j] == "R":
                red_row, red_col = i, j
            elif map[i][j] == "B":
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 1))  # 큐에 구슬의 초기 위치 추가
    visited[red_row][red_col][blue_row][blue_col] = True  # 초기 위치를 방문한 곳으로 기록

    while queue:  # 큐가 빌 때까지 반복
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()  # 현재 구슬의 위치를 받아옴
        if try_count > 10:  # 10턴이 지났을 경우 False
            break

        for i in range(4):  # 동서남북 모든 방향으로 움직인 것을 기록하기 위해 반복복 BFS
           next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], map)

            if map[next_blue_row][next_blue_col] == 'O':  # 파란 구슬이 구멍에 들어갔을 경우 실패한 것이므로 스킵
                continue
            if map[next_red_row][next_red_col] == 'O':  # 빨간 구슬이 구멍에 들어갔을 경우
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:  # 움직이는 위치가 겹칠 경우 늦게 온 구슬을 한칸 뒤로
                if r_count > b_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            if not visited[next_red_row][next_red_col][next_red_row][next_red_col]:  # 방문하지 않았을 경우
                # 이미 가본 곳은 다시 연산할 이유가 없다.
                visited[next_red_row][next_red_col][next_red_row][next_red_col] = True  # 해당 위치에 기록하고
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count))  # 큐에 현재위치 업데이트

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다.
