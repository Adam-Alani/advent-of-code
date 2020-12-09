data = [int(row.rstrip()) for row in open('input.txt').readlines()]

index = data.index(32321523)
data.pop(index)
total = 32321523
def puzzle2(data, n, total):

    n = len(data)
    for i in range(n-1):
        current = data[i]
        j = i + 1
        while j <= n :
            if current == total:
                print("Sum found between")
                print("indexes % d and % d" % (i, j - 1))
                print((min(data[i:j]) + (max(data[i:j]))))
                return 1

            if current > total or j == n:
                break

            current = current + data[j]
            j += 1
    return 0
