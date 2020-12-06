def calculate(dx, dy):
    f = [line.strip() for line in open('input/3.txt', 'r').readlines()]
    y, x, count = 0, 0, 0
    while y < len(f)-1:
        x = (x + dx) % len(f[0])
        y += dy
        count += f[y][x] == '#'
    return count

print(calculate(1,1) * calculate(3,1) * calculate(5,1) * calculate(7,1) * calculate(1,2))