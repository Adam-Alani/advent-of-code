import sys
import time
t_start = time.time()
from aocd import data

sys.setrecursionlimit(10000)
data = data.strip().split('\n')
grid = []
from collections import defaultdict
for i in range(1,len(data)-1):
    line = data[i]
    grid.append(list(line))

graph = defaultdict(set)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "#":
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != "#":
                    graph[(i, j)].add((new_x, new_y))
                    # undirected
                    graph[(new_x, new_y)].add((i, j))


graph = defaultdict(set)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "#":
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != "#":
                    graph[(i, j)].add((new_x, new_y, 1))
                    graph[(new_x, new_y)].add((i, j, 1))
while True:
    to_rem = []
    for n, e in graph.items():
        if len(e) == 2:
            to_rem.append(n)
    if not to_rem:
        break
    for n in to_rem:
        neighbors = graph[n]
        del graph[n]
        n1, n2 = neighbors
        cost = n1[2] + n2[2]
        graph[n1[:2]].remove((n + (n1[2],)))
        graph[n2[:2]].remove((n + (n2[2],)))
        graph[n1[:2]].add((n2[0], n2[1], cost))
        graph[n2[:2]].add((n1[0], n1[1], cost))

def graph_dfs(graph, x,y,cost, steps, visited):
    if x == len(grid) - 1 and y == len(grid[0]) - 2:
        return cost
    if (x,y) in visited:
        return 1
    visited.add((x,y))
    max_cost = cost
    for neigh in graph[(x,y)]:
        new_x, new_y, new_cost = neigh
        max_cost = max(max_cost, graph_dfs(graph, new_x, new_y, cost + new_cost, steps + 1, visited))
    visited.remove((x,y))
    return max_cost
print(graph_dfs(graph, 0,1, 0,0, set()) + 2)

# rows, cols = len(grid), len(grid[0])
# def is_valid_move(grid, x, y):
#     return 0 <= x < rows and 0 <= y < cols and grid[x][y] != '#'
# best = 0
# def dfs(grid, x, y, visited, steps):
#     global best
#     if x == len(grid) - 1 and y == len(grid[0]) - 2:
#         return steps
#     if (x,y) in visited:
#         return -1
#     visited.add((x,y))
#     max_steps = 0
#     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         new_x, new_y = x + dx, y + dy
#         if is_valid_move(grid, new_x, new_y) :
#             max_steps = max(max_steps,  dfs(grid, new_x, new_y, visited, steps + 1))
#     visited.remove((x,y))
#     if max_steps > best:
#         best = max_steps
#         print(best, "at: ", time.time() - t_start)
#     return max_steps
# print(dfs(grid, 0,1, set(),1))