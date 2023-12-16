from aocd import data
with open("day016") as f:
    data = f.read()
data = data.strip().split('\n')

dirs = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}

reflecs = {
    "N": {
        ".": "N",
        "-": "EW",
        "|": "N",
        "/": "E",
        "\\": "W",
    },
    "S": {
        ".": "S",
        "-": "EW",
        "|": "S",
        "/": "W",
        "\\": "E"
    },
    "E": {
        ".": "E",
        "-": "E",
        "|": "NS",
        "/": "N",
        "\\": "S",
    },
    "W": {
        ".": "W",
        "-": "W",
        "|": "NS",
        "/": "S",
        "\\": "N",
    }
}

def simulate(grid, pos, dir):
    w,h = len(grid[0]),len(grid)

    def is_valid(x, y):
        return 0 <= x < w and 0 <= y < h

    queue = [(pos, dir)]
    visited = set()

    while queue:
        temp = []
        for pos, dir in queue:
            ndir = dirs[dir]
            ndir = (pos[0] + ndir[0], pos[1] + ndir[1])
            if not is_valid(*ndir):
                continue
            for d in reflecs[dir][grid[ndir[0]][ndir[1]]]:
                if (ndir, d) in visited:
                    continue
                temp.append((ndir, d))
                visited.add((ndir, d))
        queue = temp
    return len(set([x[0] for x in visited]))


def p2(data):
    w,h = len(data[0]), len(data)
    inital = []
    for y in range(h):
        inital.append(((y, -1), "E"))
        inital.append(((y,  w), "W"))
    for x in range(w):
        inital.append(((-1, x), "S"))
        inital.append(((h,  x), "N"))
    return max(simulate(data, pos, dir) for pos, dir in inital)
print(p2(data))