T = int(input())

for t in range(T):
    N = int(input())
    nlist = list(map(int, input().split()))
    sell = nlist.pop()
    total = 0
    while len(nlist):
        temp = nlist.pop()
        if temp > sell:
            sell = temp
        elif temp < sell:
            total += sell-temp
    print(f'#{t+1} {total}')

