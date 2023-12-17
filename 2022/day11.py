import math
from aocd import data
data = data.split('\n')
monkeys = []
for i in range(0,len(data), 7):
    monkeys.append({
        "items": [int(x) for x in data[i + 1].split(":")[1].split(",")],
        "operation": data[i + 2].split(":")[1].split("=")[1].strip(),
        "test": int(data[i + 3].split(":")[1].strip().split(" ")[-1]),
        "true": int(data[i + 4].split(":")[1].strip().split(" ")[-1]),
        "false": int(data[i + 5].split(":")[1].strip().split(" ")[-1]),
        "count": 0,
    })


def simulate(monkeys):
    mod = math.lcm(*[monkey["test"] for monkey in monkeys])
    for monkey in monkeys:
        for i in range(len(monkey["items"])):
            monkey["count"] += 1
            x = monkey["items"].pop(0) % mod
            x = eval(monkey["operation"].replace("old", str(x)))
            if x % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(x)
            else:
                monkeys[monkey["false"]]["items"].append(x)
    return monkeys


rounds = 10000
for i in range(rounds):
    monkeys = simulate(monkeys)
# get the 2 monkeys with the most count
best = sorted(monkeys, key=lambda x: x["count"], reverse=True)[:2]
print(best[0]["count"] * best[1]["count"])
