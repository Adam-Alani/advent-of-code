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


grid_size = len(grid) # 131
grid_half = grid_size // 2 # 65
max_steps = grid_size * 2


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
        if (steps-1) in [grid_half, grid_half+grid_size, grid_half+grid_size*2]:
            print(steps-1, len(q))
        if steps == 0:
            return q
    print(steps, len(q))



count_paths(grid, start[0], start[1], grid_size*3)