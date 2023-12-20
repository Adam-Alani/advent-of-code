from aocd import data
import math
from collections import defaultdict
data = data.strip().split('\n')

fp = defaultdict(list)
cj = defaultdict(list)
bc = []
for line in data:
    name, children = line.split(' -> ')
    children = children.split(', ')
    if "%" in name:
        name = name[1:]
        for child in children:
            fp[name].append(child)
    elif "&" in name:
        name = name[1:]
        for child in children:
            cj[name].append(child)
    else:
        for child in children:
            bc.append(child)


def wtf(p2=False):
    low = 0
    high = 0

    fp_state = {}
    cj_mem = defaultdict(dict)
    for f in fp.keys():
        fp_state[f] = False
        for o in fp[f]:
            if o in cj.keys():
                cj_mem[o][f] = False
    for k, v in cj.items():
        for o in v:
            if o in cj.keys():
                cj_mem[o][k] = False
    child = [src for src, dst in cj.items() if "rx" in dst][0]
    seen_by_rx_src = [src for src, dst in cj.items() if child in dst]

    cycle, lows = 0, {}
    while cycle < 1000 or (p2 and len(lows) < len(seen_by_rx_src)):
        cycle += 1
        q = [("click", "bc", False)]
        while q:
            new_q = []
            for src, dst, type_ in q:

                if not type_:
                    if dst in seen_by_rx_src:
                        lows[dst] = cycle
                    low += 1
                else:
                    high += 1

                if dst == "bc":
                    for child in bc:
                        new_q.append((dst, child, type_))
                elif dst in fp.keys():
                    if not type_:
                        fp_state[dst] = not fp_state[dst]
                        for child in fp[dst]:
                            new_q.append((dst, child, fp_state[dst]))
                elif dst in cj.keys():
                    cj_mem[dst][src] = type_
                    if sum(cj_mem[dst].values()) == len(cj_mem[dst]):
                        snd = False
                    else:
                        snd = True
                    for child in cj[dst]:
                        new_q.append((dst, child, snd))
            q = new_q

    if p2:
        return math.lcm(*lows.values())
    return low * high

print(wtf())
print(wtf(True))
