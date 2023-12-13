import math

from aocd import data
from collections import defaultdict
import utils
data = data.split('\n')
dirs, dists = [], []
for line in data:
    dir, dist = line.split(' ')
    dirs.append(dir)
    dists.append(int(dist))

# neighbours = [-1, 1, -1j, 1j]
neighbours = {
    "R": 1,
    "U": 1j,
    "L": -1,
    "D": -1j
}

def sign(x):
    return 0 if x == 0 else 1 if x > 0 else -1

def simulate():
    start, seen = [0j] * 10, set()
    for dir, dist in zip(dirs, dists):
        for i in range(dist): # move rope one step at a time
            start[0] += neighbours[dir] # update head
            for j in range(1, len(start)): # update tail
                diff = start[j - 1] - start[j] # check that tail isnt on or adjacent to head
                if abs(diff) >= 2: # if not, move tail closer to head
                    start[j] += complex(sign(diff.real), sign(diff.imag)) # getting the sign is the direction (handles all cases)
            seen.add(start[-1]) # add position of tail
    print(len(seen))

simulate()