from aocd import data
import utils
data = data.split('\n')

def routine(line):
    idx = 0
    prev4 = line[:14]
    # check if all elements are unique
    if len(set(prev4)) == 14:
        return 0
    while True:
        idx += 1
        if idx + 14 > len(line):
            return 0
        prev4 = line[idx:idx+14]
        if len(set(prev4)) == 14:
            return idx + 14

    return idx + 14

for line in data:
    idx = routine(line)
    print(idx)
    if idx != 0:
        print(line[idx-1])
        break


