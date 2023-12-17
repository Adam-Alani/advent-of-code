from aocd import data
import heapq
data = data.strip().split('\n')

grid = []
for line in data:
    grid.append(list(map(int, line)))
R, C = len(grid), len(grid[0])

def djikstra(grid, step, max):
    dists = {}
    seen = set()
    q = [(0, (0, 0, (0, 0)))]
    while q:
        cost, (r, c, d) = heapq.heappop(q)
        if (r, c, d) not in seen:
            seen.add((r, c, d))
            if (r, c) == (R-1, C-1):
                return cost
            if cost > dists.get((r, c, d), 10000000):
                continue
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # can't go opposite direction
                if d == (dr, dc) or d == (-dr, -dc):
                    continue
                n_cost = cost
                for i in range(1, max+1):
                    rr = r + dr * i
                    cc = c + dc * i
                    if rr >= R or cc >= C or rr < 0 or cc < 0:
                        continue

                    n_cost += grid[rr][cc]
                    if (rr, cc, (dr, dc)) in seen:
                        continue

                    if step <= i and n_cost < dists.get((rr, cc, (dr, dc)), 10000000):
                        dists[(rr, cc, (dr, dc))] = n_cost
                        heapq.heappush(q, (n_cost, (rr, cc, (dr, dc))))

print(djikstra(grid, 1, 3))
print(djikstra(grid, 4, 10))