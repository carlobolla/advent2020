f = [line.strip() for line in open('input/1.txt', 'r').readlines()]
for lines in range(0, len(f)):
    for i in range(lines, len(f)):
        if int(f[lines]) + int(f[i]) == 2020:
            print(f[lines] + ' * ' + f[i] + ' = ' + str(int(f[lines]) * int(f[i])))
