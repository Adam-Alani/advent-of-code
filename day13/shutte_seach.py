from sympy.ntheory.modular import crt
f = open("input.txt","r").readlines()
list1 = [x for x in f[0].split(",")]

a = []
b = []
for i , val in enumerate(list1):
    if val != 'x':
        a.append(int(val))
        b.append(int(val)-i)
print(crt(a,b))