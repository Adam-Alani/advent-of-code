from itertools import product
def parse():
    data = [(pre.strip(), post.strip()) for pre, post in [line.strip().split("=") for line in open("input.txt").readlines()]]
    mem = {}
    for key , val in data:
        if key == "mask":
            mask = val
        else:
            valint = f"{int(val):036b}"
            mem[key] = int(apply(mask , valint) , base=2)
    print(sum(mem.values()))
def apply(mask , val):
    pos = [(index, val) for index, val in enumerate(mask) if val != "X"]
    for coord ,val2 in pos:
        val = val[:coord] + val2 + val[coord+1:]
    for i , val2 in pos:
        val = val[:i] + val2 + val[i+1:]
    return val