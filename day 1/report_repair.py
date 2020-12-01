data = open('input.txt', 'r').read().split('\n')
data = list(map(int, data))
def report(entries):
    hash = {}
    for i in range(1, len(entries)):
        comp = 2020 - entries[i-1] - entries[i]
        if entries[i-1] + entries[i] == 2020:
            return entries[i-1] * entries[i]
        if str(comp) in hash:
            return comp*entries[i-1]
        else:
            hash[str(entries[i-1])] = entries[i-1]
    print(hash)

def lazyreport(entries):
    for i in range(len(entries)):
        for j in range(len(entries)):
            for k in range(len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]

print(lazyreport(data))