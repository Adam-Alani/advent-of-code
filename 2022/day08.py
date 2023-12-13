from aocd import data
from collections import defaultdict
import utils
data = data.split('\n')
trees = []
for line in data:
    ints = []
    for char in line:
        ints.append(int(char))
    trees.append(ints)

visible_trees = defaultdict(int)

def is_visible(trees, i, j):
    tree = trees[i][j]
    tree_row = trees[i]
    tree_col = utils.column(trees, j)
    left = tree_row[:j]
    right = tree_row[j+1:]
    top = tree_col[:i]
    bottom = tree_col[i+1:]
    if tree > max(right) or tree > max(left) or tree > max(top) or tree > max(bottom):
        return 1
    return 0

def most_scenic(trees, i, j):
    tree = trees[i][j]
    tree_row = trees[i]
    tree_col = utils.column(trees, j)
    left = list(reversed(tree_row[:j]))
    right = tree_row[j+1:]
    top = list(reversed(tree_col[:i]))
    bottom = tree_col[i+1:]
    scores = [0,0,0,0]
    for i in range(len(left)):
        scores[0] += 1
        if left[i] >= tree:
            break

    for i in range(len(right)):
        scores[1] += 1
        if right[i] >= tree:
            break

    for i in range(len(top)):
        scores[2] += 1
        if top[i] >= tree:
            break

    for i in range(len(bottom)):
        scores[3] += 1
        if bottom[i] >= tree:
            break
    return scores[0] * scores[1] * scores[2] * scores[3]



sum = 0
sum += len(trees) * 2 + len(trees[0]) * 2 - 4
for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[0]) - 1):
        sum += is_visible(trees, i, j)

best = 0
for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[0]) - 1):
        new = most_scenic(trees, i, j)
        if new > best:
            best = new
print(best)