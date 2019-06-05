T = int(input())

for t in range(T):
    N = int(input())

    print(f'#{t+1}')
    lis = [0] * N
    lis[0] = [1]
    lis[1] = [1, 1]
    for n in range(2, N):
        li = [0] * (n+1)

        li[0] = 1

        for k in range(1, n):
            if -1<k-1<len(lis[n-1]):
                li[k] = lis[n-1][k-1]

            if -1<k<len(lis[n-1]):
                li[k] += lis[n-1][k]

        li[-1] = 1

        lis[n] = li[:]

    for i in range(N):
        for j in range(i+1):
            print(str(lis[i][j]), end=" ")
        if i <N-1:
            print()