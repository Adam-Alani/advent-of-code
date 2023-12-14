from aocd import data

data = data.split('\n')
grid = []
for line in data:
    grid.append(list(line))


def p1(grid):
    rows, cols = len(grid), len(grid[0])

    def is_valid_move(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def move_rock(x, y):
        while is_valid_move(x - 1, y) and grid[x - 1][y] == '.':
            grid[x][y], grid[x - 1][y] = grid[x - 1][y], grid[x][y]
            x, y = x - 1, y

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O':
                move_rock(i, j)
    return grid


def rotate(grid):
    list_of_tuples = zip(*grid[::-1])
    return [list(elem) for elem in list_of_tuples]


def calculate_load_after_cycles(initial_grid, num_cycles):
    seen_states, current_cycle, prev = {}, 1, None
    while current_cycle <= num_cycles:
        if prev in seen_states:
            cycle = current_cycle - seen_states[prev]
            amt = (num_cycles - current_cycle) // cycle
            current_cycle += cycle * amt
        seen_states[prev] = current_cycle

        initial_grid = rotate(p1(initial_grid))
        initial_grid = rotate(p1(initial_grid))
        initial_grid = rotate(p1(initial_grid))
        initial_grid = rotate(p1(initial_grid))

        prev = tuple(str(row) for row in initial_grid)
        current_cycle += 1

    return initial_grid


grid = calculate_load_after_cycles(grid, 1000000000)
res, leng = 0, len(grid)
for i, row in enumerate(grid):
    res += row.count('O') * (leng - i)
print(res)
