from aocd import data

data = data.split('\n')


def diff(line):
    new_line = []
    for i in range(len(line) - 1):
        new_line.append(line[i + 1] - line[i])
    return new_line


def f1(lines):
    i = 0
    while i < len(lines):
        diff_line = diff(lines[i])
        if all([x == 0 for x in diff_line]):
            lines.append(diff_line)
            break
        else:
            lines.append(diff_line)
        i = (i + 1) % len(lines)
    new = []
    for line in lines:
        line.insert(0, 0)
        # line.append(0)
        # line = line[::-1]
        new.append(line)
    for i in range(len(new) - 2, -1, -1):
        # new[i][0] = new[i][1] + new[i+1][0]
        new[i][0] = new[i][1] - new[i + 1][0]
    return new[0][0]


sum = 0
for l in data:
    l = [int(x) for x in l.split(' ')]
    sum += f1([l])
print(sum)
