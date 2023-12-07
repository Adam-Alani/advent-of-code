with open('day05') as f:
    lines = [line.rstrip() for line in f]

seeds = lines[0].split(":")[1].split()
seeds = [int(seed) for seed in seeds]
lines = lines[1:]

maps = []
i = 0
while i < len(lines):
    if lines[i].endswith("map:"):
        i += 1
        mapping = []
        while i < len(lines) and lines[i] != "":
            destination, source, range_ = lines[i].split()
            destination = int(destination)
            source = int(source)
            range_ = int(range_)
            mapping.append((destination, source, range_))
            i += 1
        maps.append(mapping)
    else:
        i += 1


def get_next(seed, map):
    for destination, source, range_ in map:
        if source <= seed < source + range_:
            return destination + seed - source
    return seed


def get_prev(location, maps):
    best = location
    for map in maps[::-1]:
        for destination, source, range_ in map:
            if destination <= best < destination + range_:
                best = source + best - destination
                break
    return best


def check_prev(seeds, best):
    for seed in seeds:
        if seed[0] <= best <= seed[1]:
            return True
    return False


# go from seed to first map -> second map -> ... -> last map
def p1(seeds):
    for map in maps:
        new_seed_locations = []
        for seed in seeds:
            new_seed_locations.append(get_next(seed, map))
        seeds = new_seed_locations
    return(min(seeds))
print(p1(seeds))


# go from location to seed
def p2(old_seeds):
    seeds = []
    for i in range(0, len(old_seeds), 2):
        seeds.append([old_seeds[i], old_seeds[i] + old_seeds[i + 1]])
    for location in range(0, int(1e8)):
        best = get_prev(location, maps)
        if check_prev(seeds, best):
            return location
print(p2(seeds))
