from functools import cmp_to_key
from aocd import data
data = data.strip().split('\n\n')

packets = [tuple(map(eval, x)) for x in [a.split() for a in data]]

def cmp(a, b):
    match a, b:
        case int(), int():
            return 1 if a > b else -1 if a < b else 0
        case int(), list():
            return cmp([a], b)
        case list(), int():
            return cmp(a, [b])
        case list(), list():
            for x,y in zip(a, b):
                res = cmp(x, y)
                if res != 0: return res
            return cmp(len(a), len(b))

res = 0
for i, p in enumerate(packets):
    x = cmp(*p)
    if x == -1:
        res += i + 1
print(res)

res = [[[2]], [[6]]]
for t in packets:
    res.extend(t)
res = sorted(res, key=cmp_to_key(cmp))
print((res.index([[2]]) + 1) * (res.index([[6]]) + 1))