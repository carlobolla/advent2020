f = [item.split('\n') for item in open('input/6.txt', 'r').read()[:-1].split('\n\n')]
total = 0
for group in f:
    result = set()
    for person in group:
        result = set(person) | result
    total += len(result)
print(total)
