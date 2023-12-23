from aocd import data
import sys

sys.setrecursionlimit(10000)
data = data.strip().split('\n')
grid = []
from collections import defaultdict
for line in data:
    grid.append(list(line))
graph = defaultdict(set)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "#":
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != "#":
                    graph[(i, j)].add((new_x, new_y, 1))
                    # undirected
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

print(graph_dfs(graph, 0,1, 0,0, set()))
