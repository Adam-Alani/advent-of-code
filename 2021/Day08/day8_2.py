from itertools import permutations

file = open("input.txt", "r")
file = file.read().strip().split("\n")

digits = {"abcdefg":8, "bcdef":5, "acdfg":2, "abcdf":3, "abd":7,
         "abcdef":9, "bcdefg":6, "abef":4, "abcdeg":0, "ab":1}

res = 0
for line in file:
    signal, output = line.split(" | ")
    signal = signal.split()
    output = output.split()

    for perm in permutations("abcdefg"):
        p = str.maketrans("abcdefg", "".join(perm))
        possible_signal = ["".join(sorted(signal.translate(p))) for signal in signal]
        possible_output = ["".join(sorted(output.translate(p))) for output in output]
        if all(signal in digits for signal in possible_signal):
            res += int("".join(str(digits[signal]) for signal in possible_output))
            break

print(res)