import sys
sys.stdin = open('magnetic.txt', 'r')

T = 10

for t in range(T):
    N = int(input())
    table = [0] * 100
    for n in range(100):
        table[n] = list(map(int, input().split()))
    move = 1
    while move != 0:
        move = 0
        for i in range(100):
            for j in range(100):
                if (table[i][j] == 1 and i == 99) or (table[i][j] == 2 and i == 0):
                    table[i][j] = 0
                    move+= 1
                elif table[i][j] == 1 and i != 99:
                    if table[i+1][j] == 0:
                        table[i][j] = 0
                        table[i+1][j] = 1
                        move += 1
                elif table[i][j] == 2 and i != 0:
                    if table[i-1][j] == 0:
                        table[i][j] = 0
                        table[i-1][j] = 2
                        move += 1

    count = 0
    for p in range(99):
        for q in range(100):
            if table[p][q] == 1 and table[p+1][q] == 2:
                count += 1
    print(f'#{t+1} {count}')