from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]

    while cony_loc < 200001:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):  # 경우의 수 때문에
            current_position, current_time = queue.popleft()

            new_time = current_time + 1

            new_positon = current_position - 1
            if new_positon >= 0 and new_time not in visited[new_positon]:
                visited[new_positon][new_time] = True
                queue.append((new_positon, new_time))

            new_positon = current_position + 1
            if new_positon < 200001 and new_time not in visited[new_positon]:
                visited[new_positon][new_time] = True
                queue.append((new_positon, new_time))

            new_positon = current_position * 2
            if new_positon < 200001 and new_time not in visited[new_positon]:
                visited[new_positon][new_time] = True
                queue.append((new_positon, new_time))

        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!
