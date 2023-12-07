from collections import defaultdict
def dfs(s, adjlists, seen=set(), visited=True):
    if s == "end": return 1
    cnt = 0
    for i in adjlists[s]:
        if i.isupper():
            cnt += dfs(i, adjlists, seen, visited)
        else:
            if i not in seen or (i != "start" and visited):
                cnt += dfs(i, adjlists, seen | {i}, visited if i not in seen else False)
    return cnt

def paths():
    file = open("input.txt", "r")
    file = file.read().strip().split("\n")
    adjlists = defaultdict(list)
    for line in file:
        a , b = line.split("-")
        adjlists[a].append(b)
        adjlists[b].append(a)

    seen = set()
    seen.add("start")
    print(dfs("start", adjlists, seen, False))
    print(dfs("start", adjlists, seen))

print(paths())