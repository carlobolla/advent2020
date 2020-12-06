pax = [line.strip() for line in open('input/5.txt', 'r').readlines()]
seats = []
for p in pax:
    start = 0
    end = 127
    seat = 0
    for i in range(0,7):
        if p[0] == 'B':
            start += (end-start)//2+1
        else:
            end -= ((end-start)//2)+1
        p=p[1:]
    seat = start*8
    start = 0
    end = 7
    for i in range(0,3):
        if p[0] == 'R':
            start += (end-start)//2+1
        else:
            end -= ((end-start)//2)+1
        p=p[1:]
    seats.append(seat+start)

print(max(seats))
print('Your seat: '+ str([x for x in range(min(seats), max(seats)) if x not in seats][0]))
