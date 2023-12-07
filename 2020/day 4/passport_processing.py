keys = ['byr' , 'iyr' , 'eyr' , 'hgt' , 'hcl' , 'ecl' , 'pid']
data = [row.strip() for row in open('input.txt').readlines()]
def convert_to_dict(data):
    passport = {}
    passports = []
    for line in data:
        if not line:
            passports.append(passport)
            passport = {}
            continue
        tuples = line.split(' ')
        for thing in tuples:
            key, val = thing.split(':')
            passport[key] = val
    if passport:
        passports.append(passport)
    return passports
passports = convert_to_dict(data)
def puzzle2(passports):
    count = 0
    for passport in passports:
        if all(x in passport for x in keys):
            if valid(passport):
                count += 1
    return count
def valid(passport):
    if 1920 <= int(passport['byr']) <= 2002:
        if 2010 <= int(passport['iyr']) <= 2020:
            if 2020 <= int(passport['eyr']) <= 2030:
                if (passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76) or (passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193):
                    if passport["hcl"][0] == '#' and all (c in '0123456789abcdef' for c in passport['hcl'][1:]):
                        if passport['ecl'] in ['amb' , 'blu' , 'brn' , 'gry' , 'grn' , 'hzl' , 'oth']:
                            if passport['pid'].isdigit() and len(passport['pid']) == 9:
                                return True
    return False
