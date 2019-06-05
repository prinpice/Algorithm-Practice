T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    puzzle = [0] * N
    for n in range(N):
        puzzle[n] = list(map(int, input().split()))

    total = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 0:
                if 1 not in puzzle[i][j:j+N]:
                    total += 1
                if 1 not in puzzle[i:i+N][j]:
                    total += 1
    print(f'#{t+1} {total}')