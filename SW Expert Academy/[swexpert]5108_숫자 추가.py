T = int(input())

for t in range(T):
    N, M, L = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = [list(map(int, input().split())) for _ in range(M)]

    for msub in mlist:
        nlist.insert(msub[0], msub[1])
    print(f'#{t+1} {nlist[L]}')
