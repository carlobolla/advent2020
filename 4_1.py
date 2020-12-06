f = [item.split('\n') for item in open('input/4.txt', 'r').read().replace(' ', '\n').split('\n\n')]
count = 0
required = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
for group in f:
    count += all([x in [item.split(':')[0] for item in group] for x in required])
print(count)
