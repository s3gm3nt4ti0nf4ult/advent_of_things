#! /usr/bin/env python3
import re

fields = set({
    'byr', 'iyr', 'eyr',
    'hgt', 'hcl', 'ecl',
    'pid'}
)

acc = 0
passports = [dict(map(lambda y: y.split(':'), x.replace('\n', ' ').split(' '))) for x in open('./input.txt').read().split('\n\n')]
valid = list(filter(lambda x: 0 if len(fields.difference(set(x.keys()))) else 1, passports))

def between(val):
    if val.endswith('cm'):
        tmp = val.replace('cm', '')
        if not tmp.isnumeric():
            return False

        return 150 <= int(tmp) <= 193

    elif val.endswith('in'):
        tmp = val.replace('in', '')
        if not tmp.isnumeric():
            return False

        return 59 <= int(tmp) <= 76


for p in valid:
    if 1920 <= int(p['byr'])  <= 2020 and \
    2010 <= int(p['iyr']) <= 2020 and \
    2020 <= int(p['eyr']) <= 2030 and \
    p['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and \
    p['pid'].isnumeric() and \
    len(p['pid']) == 9 and \
    between(p['hgt']) and \
    re.match('^#[0-9a-f]{6}', p['hcl']):
        acc += 1

print(len(valid))
print(acc)