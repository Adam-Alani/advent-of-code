with open('day04') as f:
    lines = [line.rstrip() for line in f]

def one(lines):
    winningMultiplier = {}
    sum = 0
    for line in lines:
        seenCount = 0
        left, right = line.split('|')
        left = left.split(':')[1].split()
        right = right.split()
        for num in right:
            if num in left:
                seenCount += 1
        if seenCount > 0:
            if line.split(':')[0].split()[1] not in winningMultiplier:
                winningMultiplier[line.split(':')[0].split()[1]] = seenCount
            else:
                winningMultiplier[line.split(':')[0].split()[1]] += seenCount
    for key in winningMultiplier:
        sum += int(key) * winningMultiplier[key]

    return sum


def two(lines, end):
    sum = 0
    for i, line in enumerate(lines[:end]):
        left, right = line.split('|')
        left = set(left.split(':')[1].split())
        right = set(right.split())
        count = len(left.intersection(right))
        sum += 1 + two(lines[i + 1:], count)
    return sum


print(two(lines, len(lines)))
