T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    nlist = [0] * N
    for n in range(N):
        nlist[n] = list(map(int, input().split()))
    
    maxi = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sumi = 0
            for p in range(i, i+M):
                for q in range(j, j+q):
                    sumi += nlist[p][q]
            if sumi > maxi:
                maxi = sumi

    print(f'#{t+1} {maxi}')
