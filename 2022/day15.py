from aocd import data
import z3

data = data.strip().split('\n')
sensors = []
beacons = []
for line in data:
    sensor, beacon = line.split(': closest beacon is at ')
    sensor = sensor.split('Sensor at x=')[1].split(', y=')
    sensor = tuple(map(int, sensor))
    beacon = beacon.split(', y=')
    beacon[0] = beacon[0][2:]
    beacon = tuple(map(int, beacon))
    sensors.append(sensor)
    beacons.append(beacon)


def valid(x, y, sensors, coverage):
    for sensor in sensors:
        d1 = coverage[sensor]
        d2 = manhattan_distance((x, y), sensor)
        if d2 <= d1:
            return False
    return True


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


y = 2000000


def p1():
    coverage = {}
    for beacon, sensor in zip(beacons, sensors):
        coverage[sensor] = manhattan_distance(beacon, sensor)
    res = 0
    for x in range(int(-1e7), int(1e7)):
        if not valid(x, y, sensors, coverage) and (x, y) not in beacons:
            res += 1
    return res


z = z3.Solver()
x, y = z3.Int('x'), z3.Int('y')
z.add(0 <= x)
z.add(x <= 4000000)
z.add(0 <= y)
z.add(y <= 4000000)

def zabs(x):
    return z3.If(x >= 0, x, -x)

for beacon, sensor in zip(beacons, sensors):
    dist = manhattan_distance(beacon, sensor)
    z.add(zabs(x - sensor[0]) + zabs(y - sensor[1]) > dist)

if z.check() == z3.sat:
    model = z.model()
    print(model[x] * 4000000 + model[y])
