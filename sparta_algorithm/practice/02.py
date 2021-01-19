graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
graph_2 = [1,2,3,4,5,6,7,8]
visited = []

for graph_node in graph[1]:
    print(graph_node)

for graph_node in range(graph_2):
    print(graph_node)