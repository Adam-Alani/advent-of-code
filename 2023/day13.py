from aocd import data
from utils import *
data = data.strip().split('\n')
grids = []
grid = []
for line in data:
    if line == '':
        grids.append(grid)
        grid = []
    else:
        grid.append(list(line))

grids.append(grid)

def column(matrix, i):
    return [row[i] for row in matrix]
def transpose(grid):
    return [column(grid, i) for i in range(len(grid[0]))]

def reflection(grid):
    reflection = []
    for i in range(1, len(grid)):
        bef = grid[:i]
        bef = bef[::-1]
        after = grid[i:]
        n = min(len(bef), len(after))
        bef = bef[:n]
        after = after[:n]
        if bef == after:
            reflection.append(i)
    return reflection

def p1(grid):
    reflection_points_row = reflection(grid)
    reflection_point_col = reflection(transpose(grid))
    return reflection_points_row, reflection_point_col

def smudge(grid):
    row,col = p1(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            curr = grid[i][j]
            grid[i][j] = '.' if curr == '#' else '#'
            nrow,ncol = p1(grid)
            grid[i][j] = curr

            nrow = set(nrow) - set(row)
            ncol = set(ncol) - set(col)
            if len(nrow) + len(ncol) == 1:
                return list(nrow),list(ncol)

sum = 0
for grid in grids:
    nrow,ncol = smudge(grid)
    if len(nrow) == 1:
        sum += nrow[0] * 100
    else:
        sum += ncol[0]
print(sum)

