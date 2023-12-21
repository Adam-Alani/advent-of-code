from aocd import data
data = data.strip().split('\n')

grid = []
for line in data:
    grid.append(list(line))

start = (0,0)
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == 'S':
            start = (j,i)
            grid[i][j] = '.'
            break

grid_size = len(grid) # 131
grid_half,max_steps = grid_size // 2, grid_size * 2
def count_paths(grid,x,y,steps):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = set()
    q.add((x,y))

    while steps > 0:
        nq = set()
        for x,y in q:
            for dir in dirs:
                nx,ny = x+dir[0],y+dir[1]
                if grid[ny%grid_size][nx%grid_size] == '.':
                    nq.add((nx,ny))
        q = nq
        steps -= 1
        if (steps-1) in [grid_half, grid_half+grid_size, grid_half+max_steps]:
            yield (max_steps - steps + grid_size, len(q))
        if steps == grid_half:
            break

vals = [var for var in count_paths(grid, start[0], start[1], max_steps + grid_size)]
x2,y2 = vals[0]
x1,y1 = vals[1]
x0,y0 = vals[2]
p1,p2 = (y1-y0)/(x1-x0),(y2-y1)/(x2-x1)
a,b,c = (p2-p1)/(x2-x0), p1, y0
x = 26501365
print(a*(x-x1)*(x-x0)+b*(x-x0)+c)
