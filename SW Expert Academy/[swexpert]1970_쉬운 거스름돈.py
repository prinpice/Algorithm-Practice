
T = int(input())

for t in range(T):
    money = int(input())

    dol = 50000
    li = [0]*8
    for i in range(8):
        li[i] = money//dol
        money %= dol
        if i % 2 == 0:
            dol /= 5
        else:
            dol /= 2

    print(f'#{t+1}')
    for j in range(8):
        print(li[j], end=" ")

