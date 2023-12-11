from aocd import data
import utils
data = data.split('\n')

initial, moves = {}, []
for i in range(len(data)):
    if data[i].strip().split(' ')[0].isdigit():
        data.pop(i)
        break

for line in data:
    if line == '':
        continue
    if line.startswith('move'):
        moves.append(line)
        continue

    line = list(line)
    new_line = []
    for i in range(len(line)):
        if i % 4 != 3:
            new_line.append(line[i])
    line = new_line
    for i in range(0, len(line), 3):
        if line[i+1] == '':
            continue
        key = (i + 1) // 3 + 1
        if key in initial:
            initial[key].append(line[i+1])
        else:
            if line[i+1] != ' ':
                initial[key] = [line[i+1]]

for move in moves:
    move = move.split(' ')
    quantity = int(move[1])
    from_ = int(move[3])
    to_ = int(move[5])

    elem_to_move = initial[from_][:quantity]
    print(elem_to_move)
    initial[from_] = initial[from_][quantity:]
    # initial[to_] = list(reversed(elem_to_move)) + initial[to_]
    initial[to_] = elem_to_move + initial[to_]


x = utils.keyvalues(initial)
x.sort(key=lambda x: x[0])
fin = ''
for i in range(len(x)):
    fin += str(x[i][1][0])
print(fin)

