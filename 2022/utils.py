# Returns list of integers from a string
def get_ints(line):
    return [int(x) for x in line.split(' ')]
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

