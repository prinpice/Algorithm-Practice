T = int(input())

month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for t in range(T):
    daylist = list(map(int, input().split()))
    day = 0
    if daylist[0] == daylist[2]:
        day = daylist[3] - daylist[1] +1
    else:
        day = month[daylist[0]] - daylist[1] + 1
        for mon in range(daylist[0]+1, daylist[2]):
            day += month[mon]
        day += daylist[3]
    print(f'#{t+1} {day}')