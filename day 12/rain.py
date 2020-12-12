dir = ((1, 0), (0, -1), (-1, 0), (0, 1))
pos = 10,1
curr = 0
ship = 0, 0

for row in open('input.txt').readlines():
    inst , val = row[0] , int(row[1:])
    if inst == "E":
        new = dir[0]
        pos = pos[0] + new[0]*val ,  pos[1] + new[1]*val
    if inst == "S":
        new = dir[1]
        pos = pos[0] + new[0] * val, pos[1] + new[1] * val
    if inst == "W":
        new = dir[2]
        pos = pos[0] + new[0] * val, pos[1] + new[1] * val
    if inst == "N":
        new = dir[3]
        pos = pos[0] + new[0] * val, pos[1] + new[1] * val
    if inst == "F":
        new = dir[curr]
        ship = ship[0] + pos[0] * val, ship[1] + pos[1] * val
    else:
        x , y = pos
        if inst == "R":
            if val == 90:
                pos = (y, -x)
            if val == 180:
                pos = (-x, -y)
            if val == 270:
                pos = (-y, x)
        else:
            if 360 - val == 90:
                pos = (y, -x)
            if 360 - val == 180:
                pos = (-x, -y)
            if 360 - val == 270:
                pos = (-y, x)

print(pos)
print(sum(map(abs, ship)))








