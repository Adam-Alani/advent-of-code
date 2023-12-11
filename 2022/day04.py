from aocd import data
data = data.split('\n')

count = 0
overlap = 0
for line in data:
    elf1, elf2 = line.split(',')
    lb1, ub1 = elf1.split('-')
    lb2, ub2 = elf2.split('-')
    lb1 = int(lb1)
    ub1 = int(ub1)
    lb2 = int(lb2)
    ub2 = int(ub2)
    # check if one fully contains the other
    if (lb1 <= lb2 and ub1 >= ub2) or (lb2 <= lb1 and ub2 >= ub1):
        count += 1
    # check if they overlap
    elif (lb1 <= lb2 and ub1 >= lb2) or (lb2 <= lb1 and ub2 >= lb1):
        overlap += 1

print(count)
print(overlap + count)