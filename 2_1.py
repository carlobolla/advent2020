count = 0
f = [line.strip() for line in open('input/2.txt', 'r').readlines()]
for line in f:
    splits = line.split(' ')
    password = splits[2]
    min_max = [int(x) for x in splits[0].split('-')]
    if password.count(splits[1].split(':')[0]) in range(min_max[0], min_max[1]+1):
        count += 1
print(count)