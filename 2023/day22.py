from aocd import data
data = data.strip().split('\n')

bricks = []
for line in data:
    start, end = line.split("~")
    start = tuple(int(n) for n in start.split(","))
    end = tuple(int(n) for n in end.split(","))

    block = []
    # add the range from start to end
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            for z in range(start[2], end[2]+1):
                block.append((x, y, z))
    bricks.append(block)

def drop(bricks):
    # sort by z
    bricks = sorted(bricks, key=lambda brick: min(b[2] for b in brick))
    updated,final,fell = set(),[],0
    for brick in bricks:
        dropped = False
        while True:
            one_down = set((x, y, z-1) for x, y, z in brick)
            if all((z != 0 and (x,y,z) not in updated) for x, y, z in one_down):
                brick = one_down
                dropped = True
            else:
                break

        updated.update(brick)
        final.append(brick)
        fell += dropped

    return final, fell

final, fell = drop(bricks)

p1,p2 = 0,0
for i in range(len(final)):
    changed = final.copy()
    changed.pop(i)
    _,fell = drop(changed)
    if fell == 0:
        p1 += 1
    p2 += fell
print(p1)
print(p2)