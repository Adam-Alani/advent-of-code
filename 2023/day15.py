from aocd import data
data = data.split('\n')
data = data[0].split(",")

def hash(v):
    res = 0
    for char in v:
        res += ord(char)
        res *= 17
        res %= 256
    return res

sum = 0
hmap = {}
for el in data:
    if "=" in el:
        key, value = el.split("=")
        if hmap.get(hash(key)) is None:
            hmap[hash(key)] = [(key,value)]
        else:
            if not any(key in t for t in hmap[hash(key)]):
                hmap[hash(key)].append((key,value))
            else:
                for i in range(len(hmap[hash(key)])):
                    if hmap[hash(key)][i][0] == key:
                        hmap[hash(key)][i] = (key,value)
                        break
    if "-" in el:
        key, value = el.split("-")
        for k,v in hmap.items():
            for i in range(len(v)):
                if v[i][0] == key:
                    v.pop(i)
                    break

power = 0
for k,v in hmap.items():
    for i, (key, value) in enumerate(v):
        fpower = (k + 1) * (i + 1) * int(value)
        power += fpower

print(power)
