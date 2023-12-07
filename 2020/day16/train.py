nearbyTicket  = [ list(map(int,line.split(','))) for line in open("nearby.txt").readlines() ]
myTicket = [137,173,167,139,73,67,61,179,103,113,163,71,97,101,109,59,131,127,107,53]
def parse(rule):
    name, valid = rule.split(':')
    valid = [tuple(map(int, r)) for r in (r.split('-') for r in valid.split(' or '))]
    return name, valid
with open("rules.txt") as txt:
    rules = {txt[0]: txt[1] for txt in (parse(txt) for txt in txt.read().split('\n'))}

def puzzle():
    possibilities = {}
    rest = {}
    total = 1
    validTicket = [ticket for ticket in nearbyTicket if all(any(el[0] <= n <= el[1] for v in rules.values() for el in v) for n in ticket)]
    for i in range(len(myTicket)):
        possibilities[i] = set()
        for key, val in rules.items():
            if all(any(r[0] <= t[i] <= r[1] for r in val) for t in validTicket):
                possibilities[i].add(key)
    while possibilities:
        i = next(i for i, s in possibilities.items() if len(s) == 1)
        rest[i] = next(iter(possibilities[i]))
        del possibilities[i]
        for j in possibilities:
            possibilities[j].discard(rest[i])
    for i in range(len(myTicket)):
        if "departure" in rest[i]:
            total *= myTicket[i]
    return total

print(puzzle())