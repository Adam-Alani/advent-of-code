with open('day06') as f:
    lines = [line.rstrip() for line in f]
time = lines[0].split(":")[1].split()
time = [int(t) for t in time]
distance = lines[1].split(":")[1].split()
distance = [int(d) for d in distance]

def simulate(time, dist):
    perms = []
    for hold_time in range(time):
        rem = time - hold_time
        speed = hold_time
        distance = speed * rem
        if distance > dist:
            perms.append(hold_time)
    return len(perms)

for time, distance in zip(time, distance):
    print(simulate(time, distance))

