from aocd import data
data = data.split('\n')

def f1(lines):
    i = 0
    while i < len(lines):
        diff_line = [lines[i][j + 1] - lines[i][j] for j in range(len(lines[i]) - 1)]
        lines.append(diff_line)
        if all([x == 0 for x in diff_line]):
            break
        i += 1
    # new = [[0] + list(reversed(line)) for line in lines]
    new = [[0] + line for line in lines]
    for i in range(len(new) - 2, -1, -1):
        # new[i][0] = new[i][1] + new[i+1][0]
        new[i][0] = new[i][1] - new[i + 1][0]
    return new[0][0]

sum = 0
for l in data:
    l = [int(x) for x in l.split(' ')]
    sum += f1([l])
print(sum)
