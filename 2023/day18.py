from aocd import data
data = data.strip().split('\n')

dig_plan = []
for line in data:
    action, dir, color = line.split(" ")
    dig_plan.append((action,int(dir),color))

def simulate_dig_plan(dig_plan):
    coords = [(0,0)]
    x,y = 0,0
    for action, dir, hex in dig_plan:
        hex = hex[2:]
        hex = hex[:-1]
        action = hex[-1]
        dir = hex[:-1]
        dir, action = int(dir,16),  int(action,16)
        for _ in range(dir):
            if action == 0:
                x += 1
            elif action == 2:
                x -= 1
            elif action == 3:
                y += 1
            elif action == 1:
                y -= 1
        coords.append((x,y))

    def area():
        sum = 0
        perim = 0
        for i in range(len(coords)):
            n_1 = coords[i]
            n_2 = coords[(i + 1) % len(coords)]
            x_1, y_1 = n_1
            x_2, y_2 = n_2
            sum += x_1 * y_2 - y_1 * x_2
            perim += abs(x_2 - x_1) + abs(y_2 - y_1)
        return abs(sum / 2), perim
    area, perim = area()
    # picks + bounds + 1 as they arent included in shoelace
    return int(area-perim/2 + perim + 1)

print(simulate_dig_plan(dig_plan))
