from aocd import data
data = data.split('\n')
temp = 0
best = 0
topThree = []
for line in data:
    if line == '':
        if temp > best:
            best = temp
        if len(topThree) < 3:
            topThree.append(temp)
        else:
            topThree.sort()
            if temp > topThree[0]:
                topThree[0] = temp
        temp = 0
        continue
    temp += int(line)

print(best)
print(sum(topThree))

