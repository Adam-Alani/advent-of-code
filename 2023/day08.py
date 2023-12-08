from math import lcm

with open('day08') as f:
    data = f.read().splitlines()
instructions = data[0].strip()
dirs = {}
for line in data[2:]:
    source, dest = line.split('=')
    (left, right) = dest.split(',')
    dirs[source.strip()] = (left[2:], right[1:-1])


def find():
    current, current_idx, steps = "AAA", 0, 0
    while current != "ZZZ":
        if instructions[current_idx] == 'L':
            current = dirs[current][0]
        else:
            current = dirs[current][1]
        steps += 1
        current_idx = (1 + current_idx) % len(instructions)
    return steps


def find2():
    current = []
    for key in dirs:
        if key[-1] == 'A':
            current.append(key)
    totalSteps = []
    for node in current:
        steps, current_idx = 0, 0
        while node[-1] != 'Z':
            if instructions[current_idx] == 'L':
                node = dirs[node][0]
            else:
                node = dirs[node][1]
            steps += 1
            current_idx = (1 + current_idx) % len(instructions)
        totalSteps.append(steps)
    res = totalSteps[0]
    for s in totalSteps[1:]:
        res = lcm(res, s)
    return res


print(find2())
