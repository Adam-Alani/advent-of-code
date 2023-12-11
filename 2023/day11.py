from aocd import data
from itertools import combinations
universe = data.strip().split('\n')

def column(matrix, i):
    return [row[i] for row in matrix]

def assign_numbers(expanded_universe):
    galaxy_numbers = []
    for i, row in enumerate(expanded_universe):
        for j, char in enumerate(row):
            if char == '#':
                galaxy_numbers.append((i, j))

    rows_exp = []
    for i, row in enumerate(expanded_universe):
        if row == '.' * len(row):
            rows_exp.append(i)
    cols_exp = []
    cols = [column(expanded_universe, i) for i in range(len(expanded_universe[0]))]
    for i, col in enumerate(cols):
        if col == ['.'] * len(col):
            cols_exp.append(i)

    new_stars = set()
    for star in galaxy_numbers:
        ext_r = len([r for r in rows_exp if r < star[0]])
        ext_c = len([c for c in cols_exp if c < star[1]])
        new_stars.add((star[0] + ext_r * (1000000 - 1), star[1] + ext_c * (1000000 - 1)))

    return new_stars

def sum_of_shortest_paths(galaxy_numbers):
    galaxy_combinations = combinations(galaxy_numbers, 2)
    total_length = 0
    for (start,end) in galaxy_combinations:
        total_length += abs(start[0] - end[0]) + abs(start[1] - end[1])
    return total_length


galaxy_numbers = assign_numbers(universe)
result = sum_of_shortest_paths(galaxy_numbers)
print(result)