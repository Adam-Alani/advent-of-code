from aocd import data
data = data.split('\n')

def run(data):
    cycle_vals, crt = [1], ["." for _ in range(40*6)]
    for i in range(len(data)):
        last = cycle_vals[-1]
        if "noop" in data[i]:
            cycle_vals.append(last)
        if "addx" in data[i]:
            cycle_vals.append(last)
            cycle_vals.append(last + int(data[i].split(" ")[1]))
    for i in range(len(cycle_vals)):
        x = cycle_vals[i]
        if (i%40) == x or (i%40) == x - 1 or (i%40) == x + 1:
            crt[i] = "#"
    for i in range(0, len(crt), 40):
        print("".join(crt[i:i+40]))
    return cycle_vals

cycle_vals = run(data)
res = sum([i * cycle_vals[i-1] for i in range(20, len(cycle_vals), 40)])
print(res)

