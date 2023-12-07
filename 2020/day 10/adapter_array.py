data = [int(row.rstrip()) for row in open('input.txt').readlines()].sort()
ones = 0
threes = 1
total = 0
difference = []
for i in data:
    diff = i - total
    total = i
    if diff == 1:
        ones += 1
        difference.append(1)
    if diff == 3:
        threes += 1
        difference.append(3)


lv2 = []
currlv2 = 0
prev = 0
for i in difference:
    currlv2 += 1
    if prev != i:
        currlv2 -= 1
        if prev != 0 and i != 1:
            if currlv2 != 1:
                lv2.append(currlv2)
        currlv2 = 1
    prev = i
lv2.append(currlv2)


total = 1
twoc = 0
threec = 0
fourc = 0
for i in lv2:
    if i == 2:
        twoc += 1
    elif i == 3:
        threec += 1
    elif i == 4:
        fourc += 1

for i in range(2 ,5):
    if i == 4:
        n = 7
        v = fourc
    elif i == 3:
        n = 4
        v = threec
    elif i == 2:
        n = 2
        v = twoc
    else:
        v = 1
        i = 1
    total *= (n**v)