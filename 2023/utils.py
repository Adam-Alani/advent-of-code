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


from heapq import heappop, heappush
def dijkstra(grid, neighbour_func, q=None):
    if q is None:
        q = [(0, (0, 0))]
    R, C = len(grid), len(grid[0])
    # MODIFY THIS TO FIT YOUR NEEDS, expand the state
    # generic state
    seen = set()
    costs = {}
    while q:
        cost, (state) = heappop(q)
        if state[0] == R-1 and state[1] == C-1:
            return cost
        if state in seen:
            continue
        if cost > costs.get(state, 10000000):
            continue

        seen.add((state[0],state[1]))

        for neighbour in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_cost = cost
            for new_state in neighbour_func(state, R, C, neighbour=neighbour):
                new_cost += grid[new_state[0]][new_state[1]]
                if new_state not in seen and new_cost < costs.get(new_state, 10000000):
                    costs[new_state] = new_cost
                    heappush(q, (new_cost, new_state))
    return costs


def neighbour(state, W, H, neighbour=None):
    x, y = state
    dx, dy = neighbour
    rr = x + dx
    cc = y + dy
    if rr >= H or cc >= W or rr < 0 or cc < 0:
        return
    yield (rr, cc)


def shoelace(coords):
    """
    Shoelace formula for area of polygon
    :param coords: list of coordinates (x,y)
    :return: area of polygon
    """
    # sum = 0
    # for i in range(len(coords)):
    #     n_1 = coords[i]
    #     n_2 = coords[(i + 1) % len(coords)]
    #     x_1, y_1 = n_1
    #     x_2, y_2 = n_2
    #     sum += x_1 * y_2 - y_1 * x_2
    # return abs(sum / 2)
    return abs(sum([x_1 * y_2 - y_1 * x_2 for (x_1, y_1), (x_2, y_2) in zip(coords, coords[1:] + [coords[0]])]) / 2)