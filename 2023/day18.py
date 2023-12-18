from aocd import data
import utils

data = data.strip().split('\n')

dig_plan = []
for line in data:
    action, dir, color = line.split(" ")
    dig_plan.append((action, int(dir), color))


def simulate_dig_plan(dig_plan):
    coords, x, y, p = [(0, 0)], 0, 0, 0
    for action, dir, hex in dig_plan:
        hex = hex[2:]
        hex = hex[:-1]
        action = hex[-1]
        dir = hex[:-1]
        dir, action = int(dir, 16), int(action, 16)
        if action == 0:
            x += dir
        elif action == 2:
            x -= dir
        elif action == 3:
            y += dir
        elif action == 1:
            y -= dir
        p += dir
        coords.append((x, y))

    area = utils.shoelace(coords)
    # picks + bounds + 1 as they arent included in shoelace
    return int(area - p / 2 + p + 1)


print(simulate_dig_plan(dig_plan))
