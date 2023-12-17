import functools
from aocd import data
data = data.strip().split('\n')
rates = {}  # rates[valve] = rate
tunnels = {}  # tunnels[start] = [end1, end2, ...]
for line in data:
    valve = line[6:8]
    rate = int(line.split("=")[1].split(";")[0])
    _, t = line.split(";")
    t = t.replace("valves", "valve")[len(" tunnels lead to valve "):]
    t = t.split(", ")
    tunnels[valve] = t
    rates[valve] = rate
print(tunnels)
print(rates)

@functools.lru_cache(maxsize=None)
def best_path(min=30, curr="AA", opened=()):
    if min <= 0:
        return 0
    pressure = rates[curr] * (min-1)
    optimal = 0
    for tunnel in tunnels[curr]:
        if curr not in opened and pressure != 0:
            optimal = max(optimal, pressure + best_path(min-2, tunnel, (*opened, curr)))
        optimal = max(optimal, best_path(min - 1, tunnel, opened))
    return optimal
# print(best_path())

def next(path, opened):
    curr, res = path[-1], []
    # do kinda same as the recursive function above
    if curr not in opened and rates[curr] != 0:
        new_opened = opened.copy()
        new_opened.add(curr)
        res.append((path + [curr], new_opened))
    for tunnel in tunnels[curr]:
        res.append((path + [tunnel], opened))
    return res

def elephant_best_path(start="AA"):
    stack = [(0, ([start], [start]), set())]
    for i in range(26):
        stack = list(reversed(sorted(stack)))[:10000]
        new_stack = []
        for pressure, (me, e), opened in stack:
            pressure += sum(rates[x] for x in opened)
            for me_p, me_op in next(me, opened):
                for e_p, e_op in next(e, me_op):
                    new_stack.append((pressure, (me_p, e_p), e_op))
        stack = new_stack
    return max(stack)[0]


print(elephant_best_path())

