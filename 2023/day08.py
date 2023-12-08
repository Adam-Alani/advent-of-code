from math import lcm
with open('day08') as f:
    data = f.read().splitlines()
instructions = data[0].strip()
dict = {}
for line in data[2:]:
    line = line.split('=')
    line[0] = line[0].strip()
    (left, right) = line[1].split(',')
    left = left[2:]
    right = right[1:-1]
    dict[line[0]] = (left, right)

def find():
    current,current_idx,steps  = "AAA", 0, 0
    while current != "ZZZ":
        if instructions[current_idx] == 'L': current = dict[current][0]
        else: current = dict[current][1]
        steps += 1
        current_idx = (1 + current_idx) % len(instructions)
    return steps

def find2():
    current = []
    for key in dict:
        if key[-1] == 'A':
            current.append(key)
    totalSteps = []
    for node in current:
        steps,current_idx = 0,0
        while node[-1] != 'Z':
            if instructions[current_idx] == 'L': node = dict[node][0]
            else: node = dict[node][1]
            steps += 1
            current_idx = (1 + current_idx) % len(instructions)
        totalSteps.append(steps)
    res = totalSteps[0]
    for s in totalSteps[1:]:
        res = lcm(res, s)
    return res
print(find2())