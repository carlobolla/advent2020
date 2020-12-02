f = [int(line.strip()) for line in open('input/1.txt', 'r').readlines()]
for line in f:
    for i in range(f.index(line), len(f)):
        if line + f[i] == 2020:
            print(str(line) + ' * ' + str(f[i]) + ' = ' + str(line * f[i]))
            exit(0)