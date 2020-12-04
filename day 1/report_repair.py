data = open('input.txt', 'r').read().split('\n')
data = list(map(int, data))

def report(entries):
    hash = {}
    for i in range(len(entries)):
        comp = 2020 - entries[i]
        if str(comp) in hash:
            return comp*entries[i]
        else:
            hash[str(entries[i])] = entries[i]

