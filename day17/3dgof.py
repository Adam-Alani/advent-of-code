from collections import defaultdict
def neighbours(pos):
    res = []
    x , y , z , l = pos
    for i in range(-1 , 2):
        for j in range(-1, 2):
            for k in range(-1 , 2):
                for frth in range(-1, 2):
                    if not (i == j == k == frth == 0):
                        res.append((x+i , y+j , z+k , frth+l))
    return res
with open('input.txt') as gameBoard:
    line = 0
    coords = defaultdict(lambda: False)
    while line < 8:
        board = gameBoard.readline().strip()
        temp = list(board)
        for i in range(len(temp)):
            pos = i , line , 0 , 0
            coords[pos] = temp[i] == '#'
            for neigh in neighbours(pos):
                coords[neigh]
        line += 1
c = 6
while c != 0:
    curr = list(coords.keys())
    arr = []
    for pos in curr:
        countNeigh = 0
        for neigh in neighbours(pos):
            countNeigh += coords[neigh]
        if coords[pos] and countNeigh not in [2,3]:
            arr.append(pos)
        elif countNeigh == 3 and not coords[pos] :
            arr.append(pos)
    for i in arr:
        coords[i] = not coords[i]
    c -= 1
res = 0
for i in coords.values():
    res += i
