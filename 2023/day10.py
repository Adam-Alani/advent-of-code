with open('day10') as f:
    grid = f.read().splitlines()

def find_loop(grid, start):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    stack = [(start, None)]
    steps = 0
    while stack:
        current, prev_direction = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        pipe = grid[current[0]][current[1]]
        if pipe == '.':
            continue

        possible_directions = []
        if pipe == 'S':
            possible_directions = range(4)
        elif pipe == '|':
            possible_directions = [1, 3]
        elif pipe == '-':
            possible_directions = [0, 2]
        elif pipe == 'L':
            possible_directions = [0, 3]
        elif pipe == 'J':
            possible_directions = [2, 3]
        elif pipe == '7':
            possible_directions = [1, 2]
        elif pipe == 'F':
            possible_directions = [0, 1]

        for i in possible_directions:
            direction = directions[i]
            next_pos = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]):
                next_pipe = grid[next_pos[0]][next_pos[1]]
                if next_pipe != '.' and (next_pos, direction) != prev_direction:
                    stack.append((next_pos, (next_pos, direction)))
        steps += 1
    print(steps // 2)
    return visited

start = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i, j)

loop = find_loop(grid, start)
c = 0
for i in range(len(grid)):
    north = 0
    for j in range(len(grid[i])):
        curr = grid[i][j]
        if (i,j) in loop:
            north += 1 if curr in {"|", "L", "J", "S"} else 0
        elif north % 2 == 1:
            c += 1
print(c)




