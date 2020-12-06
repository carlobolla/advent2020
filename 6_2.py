f = [item.split('\n') for item in open('input/6.txt', 'r').read()[:-1].split('\n\n')]
total = 0
for group in f:
    result = set(group[0])
    for person in group[1:]:
        result = set(person).intersection(result)
    total += len(result)
    print(result)
print(total)
