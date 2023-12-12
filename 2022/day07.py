from aocd import data
from collections import defaultdict
import utils
data = data.split('\n')

sizes = {}
stack = []
for line in data:
    if line.startswith('$ cd'):
        dest = line.split(' ')[2]
        if dest == "..":
            stack.pop()
        else:
            path = stack[-1] + '/' + dest if len(stack) > 0 else dest
            stack.append(path[1:])
    elif line.startswith('$ ls'):
        continue
    elif line.startswith("dir "):
        continue
    else:
        size, name = line.split(' ')
        for dir in stack:
            if dir in sizes:
                sizes[dir] += int(size)
            else:
                sizes[dir] = int(size)

total = 70000000
needed = 30000000
sorted_sizes = utils.keyvalues(sizes)
sorted_sizes.sort(key=lambda x: x[1])
used = sorted_sizes[-1][1]

for i in range(len(sorted_sizes)):
    unused = total - used
    if unused + sorted_sizes[i][1] >= needed:
        print(sorted_sizes[i][1])
        break

sum = 0
for size in sizes.values():
    sum += size if size <= 100_000 else 0
print(sum)

