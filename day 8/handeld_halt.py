data = list(open('input.txt').read().split('\n'))
def halt(data):
    acc = 0
    i = 0
    passed = set()
    while True:
        if i in passed:
            return(acc)
        passed.add(i) 
        step, val = data[i].split()
        val = int(val)
            
        if step == "jmp":
            i += val
        elif step == "acc":
            acc += val
            i += 1
        elif step == "nop":
            i += 1
def secondHalt(data):
    acc = 0
    i = 0
    passed = set()
    while True:
        if i == len(data):
            return(acc)
        if i in passed:
            return None
        passed.add(i) 
        step, val = data[i].split()
        val = int(val)
            
        if step == "jmp":
            i += val
        elif step == "acc":
            acc += val
            i += 1
        elif step == "nop":
            i += 1
def backTrack(data):
    for i in range(len(data)):
        copy = data[:]
        if copy[i][:3] == "nop":
            copy[i] = copy[i].replace("nop" , "jmp")
        elif copy[i][:3] == "jmp":
            copy[i] = copy[i].replace("jmp" , "nop" )
        res = secondHalt(copy)
        if res:
            return(res)
