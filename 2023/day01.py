with open("day01") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

def one(lines):
    import re
    pattern = '^\D*(\d).*?(\d)?\D*$'
    return sum(int(m.group(1) + (m.group(2) if m.group(2) else m.group(1))) for line in lines if
                     (m := re.search(pattern, line)))

def two(lines):
    string_to_number = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    def convert(line):
        result = ""
        for i, c in enumerate(line):
            if c.isdigit():
                result += c
            for k in string_to_number.keys():
                if line[i:].startswith(k):
                    result += str(string_to_number[k])
                    break
        return result
    return one([convert(line) for line in lines])


print(two(lines))
# print(convert("eightwothree"))
