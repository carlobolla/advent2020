count = 0
f = [line.strip() for line in open('input/2.txt', 'r').readlines()]
for line in f:
    splits = line.split(' ')
    password = splits[2]
    positions = [int(x) for x in splits[0].split('-')]
    if bool(password[positions[0]-1] == splits[1].split(':')[0]) ^ bool(password[positions[1]-1] == splits[1].split(':')[0]):
        count += 1
print(count)