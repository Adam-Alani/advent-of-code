from aocd import data
data = data.split('\n')

sum = 0
for line in data:
    l = len(line) // 2
    comp1 = set(line[:l])
    comp2 = set(line[l:])
    common = comp1.intersection(comp2)
    for char in common:
        if char.islower():
            sum += ord(char) - 96
        else:
            sum += ord(char) - 64 + 26
print(sum)

sum = 0
for i in range(0, len(data), 3):
    lines = data[i:i+3]
    l1 = set(lines[0])
    l2 = set(lines[1])
    l3 = set(lines[2])
    common = l1.intersection(l2).intersection(l3)
    for char in common:
        if char.islower():
            sum += ord(char) - 96
        else:
            sum += ord(char) - 64 + 26
print(sum)

