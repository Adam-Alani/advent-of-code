import re
data = open('input.txt', 'r').read().split('\n')
data = list(data)

test = ['1-3 a: abcde' , '1-3 b: cdefg' , '2-9 c: ccccccccc']
def validpass(data):
    res = 0
    for i in range(len(data)):
        range1 = re.split(r"([a-z])", data[i], 1, flags=re.I)[0].split("-")
        range1 = list(map(int, range1))
        stc , str1 = re.split(r"([a-z])", data[i], 1, flags=re.I)[1:]

        if range1[0] <= str1.count(stc) <= range1[1]:
            res += 1
    return res

def validpos(data):
    res = 0
    for i in range(len(data)):
        range1 = re.split(r"([a-z])", data[i], 1, flags=re.I)[0].split("-")
        range1 = list(map(int, range1))
        stc , str1 = re.split(r"([a-z])", data[i], 1, flags=re.I)[1:]
        str1 = str1[1:]
        c = 0
        for j in range(len(str1)):
            if str1[j] == stc and range1[0] == j:
                c += 1
            if str1[j] == stc and range1[1] == j:
                c += 1
        if c == 1:
            res += 1
    return res

print(validpos(data))