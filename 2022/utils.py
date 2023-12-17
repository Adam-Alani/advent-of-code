# Returns list of integers from a string
def get_ints(line, delim=' '):
    return [int(x) for x in line.split(delim)]
# Return grid thats also padded with pad
def get_grid(lines, pad=0):
    grid = []
    for line in lines:
        grid.append([pad] + get_ints(line) + [pad])
    grid = [[pad] * len(grid[0])] + grid + [[pad] * len(grid[0])]
    return grid
# Returns list of differences between consecutive elements
def list_diff(x):
    return [b-a for a, b in zip(x, x[1:])]
# Flatten list of lists
def flatten(l):
    return [i for x in l for i in x]
# Returns list of key-value pairs from dictionary
def keyvalues(d):
    return list(d.items())
# Returns column i of matrix
def column(matrix, i):
    return [row[i] for row in matrix]
# Returns transpose of matrix
def transpose(grid):
    return [column(grid, i) for i in range(len(grid[0]))]

def min_max(x,y):
    return min(x,y), max(x,y)

from collections import defaultdict
from heapq import heappop, heappush

