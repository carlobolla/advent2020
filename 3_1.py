f = [line.strip() for line in open('input/3.txt', 'r').readlines()]
y, x, count = 0, 0, 0
while y < len(f)-1:
    x = (x + 3) % len(f[0])
    y += 1
    count += f[y][x] == '#'
print(count)
