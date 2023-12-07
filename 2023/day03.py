def get_input():
    with open("day03") as f:
        return [list(line.strip()) for line in f.readlines()]


neighbours = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]


def get_numbers(arr):
    gears = []
    for i, row in enumerate(arr):
        for j, c in enumerate(row):
            if c == "*":
                numbers = []
                for x, y in neighbours:
                    try:
                        if arr[i + x][j + y].isdigit():
                            numbers.append(get_full_number(arr, i + x, j + y))
                    except IndexError:
                        pass
                if len(numbers) == 2:
                    gears.append(numbers[0] * numbers[1])
    return gears


def get_full_number(arr, i, j):
    number = ""
    dj = j
    while j >= 0 and arr[i][j].isdigit():
        number = arr[i][j] + number
        arr[i][j] = " "
        j -= 1
    j = dj + 1
    while j < len(arr[i]) and arr[i][j].isdigit():
        number += arr[i][j]
        arr[i][j] = " "
        j += 1
    return int(number)


print(sum(get_numbers(get_input())))
