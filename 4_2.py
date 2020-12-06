import re

def validate(group):
    fields = dict(item.split(':') for item in group)
    if not re.match(r'^(19[2-9][0-9]|200[0-2])$', fields['byr']): return False
    if not re.match(r'^(201[0-9]|2020)$', fields['iyr']): return False
    if not re.match(r'^(202[0-9]|2030)$', fields['eyr']): return False
    if not re.match(r'^((59|6[0-9]|7[0-6]))in|(1[5-9][0-9]cm)$', fields['hgt']): return False
    if not re.match(r'^#([0-9]|[a-f]){6}$', fields['hcl']): return False
    if not fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False
    if not re.match(r'^\d{9}$', fields['pid']): return False
    return True


f = [item.split('\n') for item in open('input/4.txt', 'r').read()[:-1].replace(' ', '\n').split('\n\n')]
count = 0
required = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
for group in f:
    if all([x in [item.split(':')[0] for item in group] for x in required]):
        count += validate(group)
print(count)
