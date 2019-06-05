T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxi = 0
    temp = 0
    if N > M:
        for m in range(N-M+1):
            for i in range(M):
                temp += A[m+i]*B[i]
            if maxi < temp:
                maxi = temp
    else:
        for n in range(M-N+1):
            for j in range(N):
                temp += B[n+j]* A[j]
            if maxi < temp:
                maxi = temp
    print(f'#{t+1} {temp}')
