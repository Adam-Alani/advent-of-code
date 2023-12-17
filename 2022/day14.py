from aocd import data
data = data.strip().split('\n')
from utils import min_max

lowest = 0
walls = set()
for line in data:
    loc = []
    tups = line.split(" -> ")
    for tup in tups:
        loc.append(tuple(map(eval, tup.split(","))))

    for (x1,y1), (x2,y2) in zip(loc, loc[1:]):
        x1,x2 = min_max(x1,x2)
        y1,y2 = min_max(y1,y2)

        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                print(x,y)
                lowest = max(lowest, y+1)
                walls.add(complex(x,y))

res = 0
while complex(500, 0) not in walls:
    sand = complex(500, 0)
    while True:
        if sand.imag >= lowest:
            break
        elif sand + 1j not in walls:
            sand += 1j
        elif sand -1 + 1j not in walls:
            sand += -1 + 1j
        elif sand + 1 + 1j not in walls:
            sand += 1 + 1j
        else:
            break
    walls.add(sand)
    res += 1
print(res)
