import functools
from aocd import data, submit
data = data.strip().split('\n')
test = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
""".strip().split('\n')

def get_rock(t, y):
    # always return 2 squares from the left
    if t == 0:
        return {(2, y), (3, y), (4, y), (5, y)}
    elif t == 1:
        return {(3, y+2), (2, y+1), (3, y+1), (4, y+1), (3, y)}
    elif t == 2:
        return {(4, y+2), (4, y+1), (4, y), (2, y), (3, y)}
    elif t == 3:
        return {(2, y+3), (2, y+2), (2, y+1), (2, y)}
    elif t == 4:
        return {(2, y), (3, y), (2, y+1), (3, y+1)}
    else:
        raise ValueError(t)

def move_right(rock):
    if any(x == 6 for x, y in rock):
        return rock
    return {(x+1, y) for x, y in rock}

def move_left(rock):
    if any(x == 0 for x, y in rock):
        return rock
    return {(x-1, y) for x, y in rock}

def move_down(rock):
    return {(x, y-1) for x, y in rock}

def move_up(rock):
    return {(x, y+1) for x, y in rock}

def stringify(CAVE):
    # get biggest y
    stringify = ""
    maxy = max(y for x, y in CAVE)
    for y in range(maxy, maxy-8, -1):
        for x in range(7):
            if (x, y) in CAVE:
                stringify += "#"
            else:
                stringify += "."
        stringify += "\n"
    return stringify
def p1(data):
    data= data[0]
    top = 4
    ptr = 0
    CAVE = set([(x, 0) for x in range(7)])
    seen = {}
    cycle = 0
    i = 0
    m_r = 1000000000000
    # m_r = 9
    while i < m_r:
        t = i % 5
        rock = get_rock(t, top)
        while True:
            if data[ptr] == ">":
                rock = move_right(rock)
                if CAVE & rock:
                    rock = move_left(rock)
            else:
                rock = move_left(rock)
                if CAVE & rock:
                    rock = move_right(rock)
            ptr = (ptr + 1) % len(data)
            rock = move_down(rock)
            if rock & CAVE:
                rock = move_up(rock)
                CAVE |= rock
                i += 1
                max_y = max(y for x, y in CAVE)
                top = max_y + 4
                if max_y < 8:
                    break
                last8 = [(x, y) for x, y in CAVE if y >= max_y - 7]
                state = (stringify(last8), t, ptr)
                if state in seen:
                    (old_i, old_y) = seen[state]
                    new_cycle = i - old_i
                    skip = (m_r - i) // new_cycle
                    i += skip * new_cycle
                    cycle += skip * (max_y - old_y)
                    seen = {}
                else:
                    seen[state] = (i, max_y)
                break
    # return highest rock
    print(max(y for x, y in CAVE) + cycle)
    return max(y for x, y in CAVE)

p1(data)
# assert p1(test) == 1514285714288
# submit(p1(data),part="b",year=2022)