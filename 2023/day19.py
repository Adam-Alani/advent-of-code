from aocd import data
data = data.strip().split('\n')
workflows, ratings = {}, []
curr = "in"
rate = False
for line in data:
    if line == "":
        rate = True
        continue
    if rate:
        line = line.split("{")[1].split("}")[0].split(",")
        for i in line:
            i = i.split("=")
            if i[0] == "x":
                x = int(i[1])
            elif i[0] == "m":
                m = int(i[1])
            elif i[0] == "a":
                a = int(i[1])
            elif i[0] == "s":
                s = int(i[1])
        ratings.append([x, m, a, s])
    else:
        line = line.split('{')
        name = line[0]
        line = line[1].split('}')
        line = line[0].split(',')
        workflows[name] = line

def process_part(part):
    curr = "in"

    x,m,a,s = part
    while True:
        if curr == "R":
            return "R"
        elif curr == "A":
            return "A"
        rules = workflows[curr]

        idx = 0
        while idx < len(rules):

            rule = rules[idx]
            try:
                condition, next = rule.split(":")
                condition = condition.replace("{", "").replace("}", "")

                if eval(condition, {"x": x, "m": m, "a": a, "s": s}):
                    if next == "R": return "R"
                    elif next == "A": return "A"
                    else: curr = next
                    break
                else:
                    idx += 1
            except:
                curr = rule
                idx += 1


def get_ranges(rng, gt, val):
    if gt:
        return tuple(filter(lambda x: x > val, rng))
    return tuple(filter(lambda x: x < val, rng))

def p2(x,m,a,s,curr):
    if curr == "R":
        return 0
    elif curr == "A":
        return len(x) * len(m) * len(a) * len(s)

    rules, res = workflows[curr], 0
    for rule in rules:
        if ":" in rule:
            condition, next = rule.split(":")
            condition = condition.replace("{", "").replace("}", "")

            gt = False
            if "<" in condition:
                var, val = condition.split("<")
                val = int(val)
            else:
                var, val = condition.split(">")
                val = int(val)
                gt = True

            if var == "x":
                new_x = get_ranges(x, gt, val)
                if len(new_x) != 0:
                    res += p2(new_x, m, a, s, next)
                x = get_ranges(x, not gt, val + 1 if gt else val - 1)
            elif var == "m":
                new_m = get_ranges(m, gt, val)
                if len(new_m) != 0:
                    res += p2(x, new_m, a, s, next)
                m = get_ranges(m, not gt,  val + 1 if gt else val - 1 )
            elif var == "a":
                new_a = get_ranges(a, gt, val)
                if len(new_a) != 0:
                    res += p2(x, m, new_a, s, next)
                a = get_ranges(a, not gt, val + 1 if gt else val - 1)
            elif var == "s":
                new_s = get_ranges(s, gt, val)
                if len(new_s) != 0:
                    res += p2(x, m, a, new_s, next)
                s = get_ranges(s, not gt, val + 1 if gt else val - 1)
        else:
            res += p2(x, m, a, s, rule)
    return res

print(p2(
        tuple(range(1, 4001)),
        tuple(range(1, 4001)),
        tuple(range(1, 4001)),
        tuple(range(1, 4001)),
        "in"
))
