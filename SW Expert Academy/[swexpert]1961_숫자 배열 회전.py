
T = int(input())
for t in range(T):
    N = int(input())
    li = [0]*N

    result = [[""]*N for i in range(N)]
    for n in range(N):
        li[n] = list(input().split())
    for j in range(N):
        for k in range(N-1, -1, -1):
            result[j][0] += str(li[k][j])
            # print(result[j][i], [k][j])
            result[j][1] += str(li[N-j-1][k])
            result[j][2] += str(li[N-k-1][N-j-1])
    print(f'#{t+1}')
    for i in range(N):
        for p in range(N):
            print(result[i][p], end=" ")
        print()
    