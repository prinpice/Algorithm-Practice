T = int(input())
print(type(T))
for t in range(T):
    N = int(input())
    templist = list(map(int, input().split()))
    nlist = [0] * N
    for n in range(N):
        nlist[n] = abs(0-templist[n])
        print(nlist)
    mini = min(nlist)
    minn = nlist.count(mini)
    print(f'#{t+1} {mini} {minn}')