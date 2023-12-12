import functools

from aocd import data
from utils import *
data = data.strip().split('\n')
gears, pos = [], []
for line in data:
    line = line.split(' ')
    gears.append(line[0])
    pos.append(get_ints(line[1], delim=','))

def get_arrangements(p, d):
    @functools.cache
    def get(pattern, length, data):
        if len(data) == 0: # we reached the end
            if any(x == '#' for x in pattern):
                return 0
            return 1
        head, tail = data[0], data[1:]
        rem = sum(tail) + len(tail)
        # basically slides a subpattern with curr amount hashtags over the pattern until it fits
        count = 0
        for i in range(length-rem-head+1):
            opt = '.' * i + '#' * head + '.'
            # if it fits, recurse on the rest of the pattern
            if all((a == b or a == '?') for a, b in zip(pattern, opt)):
                rest_p = pattern[len(opt):]
                # gets the number of times everything matches
                count += get(rest_p, len(rest_p), tail)
        return count
    return get(p, len(p), tuple(d))


res = 0
for gear, p in zip(gears, pos):
    # res += get_arrangements(gear,p)
    res += get_arrangements('?'.join((gear,gear,gear,gear,gear)),p*5)
print(res)
