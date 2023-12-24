from aocd import data
data = data.strip().split('\n')

small = 200000000000000
big = 400000000000000

coords = []
for line in data:
    pos, vel = line.split("@")
    pos = pos.strip().split(",")
    vel = vel.strip().split(",")
    pos = [int(x) for x in pos]
    vel = [int(x) for x in vel]
    coords.append((*pos, *vel))

def equation(h1, h2):
    x1,y1,_,xv1,yv1,_ = h1
    x2,y2,_,xv2,yv2,_ = h2
    h1_slope =  yv1 / xv1
    h2_slope = yv2 / xv2

    if h1_slope == h2_slope:
        return False

    s1 = y1 - h1_slope * x1
    s2 = y2 - h2_slope * x2

    slope = (s2 - s1) / (h1_slope - h2_slope)
    y = slope * h1_slope + s1

    intersects = (slope > x1) == (xv1 > 0) and (slope > x2) == (xv2 > 0)
    if not intersects:
        return False

    if small <= slope <= big and small <= y <= big:
        return True
    return False

count = 0
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        count += equation(coords[i], coords[j])
print(count)

import z3

x,y,z, xv,yv,zv = z3.Ints('x y z xv yv zv')
s = z3.Solver()
for i, h in enumerate(coords):
    t = z3.Int(f"t{i}")
    s.add(t > 0)
    s.add(x + xv * t == h[0] + h[3] * t)
    s.add(y + yv * t == h[1] + h[4] * t)
    s.add(z + zv * t == h[2] + h[5] * t)
s.check()
total = sum(s.model()[v].as_long() for v in [x,y,z])
print(total)