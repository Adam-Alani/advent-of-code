from collections import Counter
from functools import cmp_to_key
with open('day07') as f:
    lines = [line.rstrip().split() for line in f]

def get_rank(h):
    c = Counter(h)
    if "J" in h:
        jc = c["J"]
        del c["J"]
        if len(c) == 0:
            c["A"] = 5
        else:
            cmn,_ = c.most_common()[0]
            c[cmn] += jc
    if len(c) == 1:
        return 7
    cmn = c.most_common()
    if cmn[0][1] == 4:
        return 6
    if len(c) == 2 and 3 in c.values():
        return 5
    if 3 in c.values():
        return 4
    if cmn[0][1] == 2:
        if cmn[1][1] == 2:
            return 3
        else:
            return 2
    return 1


vals = "J23456789TQKA"
def cmp(a, b):
    a = a[0]
    b = b[0]
    ra = get_rank(a)
    rb = get_rank(b)

    if ra > rb:
        return 1
    elif ra < rb:
        return -1
    for card1, card2 in zip(a, b):
        if vals.index(card1) > vals.index(card2):
            return 1
        elif vals.index(card1) < vals.index(card2):
            return -1
    return 0

def simulate(input):
    sorted_hands = sorted(input, key=cmp_to_key(cmp))
    res = 0
    for rank, (hand, bid) in enumerate(sorted_hands, start=1):
        res += int(rank) * int(bid)
    print(res)
simulate(lines)




