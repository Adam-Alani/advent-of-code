data = [row.rstrip() for row in open('input.txt').readlines()]
bagdict = {}
def parse(data):
    for row in data:
        outside = row.rsplit(' bags contain ')
        outsidedict = {}
        for nested in outside[1].rsplit(', '):
            words = nested.rsplit(' ')
            if words[0] == 'no':
                continue
            else:
                outsidedict[words[1] + ' ' + words[2]] = int(words[0])
        bagdict[outside[0]] = outsidedict
    return bagdict
bagdict = parse(data)
def puzzle1(bagdict):
    bag_to_find = set(['shiny gold'])
    next_gen = 0
    while len(bag_to_find) != next_gen:
        next_gen = len(bag_to_find)
        #print(next_gen)
        for key in bagdict:
            if any(setbag in bagdict[key].keys() for setbag in bag_to_find):
                bag_to_find.add(key)
    print(len(bag_to_find))
    pass
def puzzle2(color):
    return 1 + sum(puzzle2(sub_c) * bagdict[color][sub_c] for sub_c in bagdict[color])
