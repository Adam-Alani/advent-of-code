with open("input.txt") as inputs:
    group = [row for row in inputs.read()[:-1].split("\n")]
total = 0
set = {}
c = 0
for line in group:
    if len(line) > 0:
        c += 1
        for char in line:
            try:
                set[char] += 1
            except Exception:
                set[char] = 1
    else:
        for key, value in set.items():
            if c == value:
                total += 1
        c =0
        set = {}
