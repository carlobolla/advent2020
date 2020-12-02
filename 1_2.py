f = [int(line.strip()) for line in open('input/1.txt', 'r').readlines()]
for lines_1 in range(0, len(f)):
    for lines_2 in range(lines_1, len(f)):
        for i in range(lines_2, len(f)):
            if f[lines_1] + f[lines_2] + f[i] == 2020:
                print(str(f[lines_1]) + ' * ' + str(f[lines_2]) + ' * ' + str(f[i]) + ' = ' + str(f[lines_1] * f[lines_2] * f[i]))
                exit(0)
