def mycir(b):
    if len(b) == 0 or len(b) == 1:
        return True
    elif b[0] == b[len(b) - 1]:
        p = ""
        for k in range(1, len(b) - 1):
            p += b[k]
        return mycir(p)
    else:
        return False


TC = int(input())

for tc in range(TC):
    N, M = map(int, input().split())
    result = ""

    li = []
    for i in range(N):
        s = input()
        li += [s]

    dx = [0, 0, -(M - 1), M - 1]  # 상하좌우
    dy = [-(M - 1), M - 1, 0, 0]

    for x in range(N):
        for y in range(N):
            a = li[x][y]
            for mode in range(4):
                testX = x + dx[mode]
                testY = y + dy[mode]
                if (testX >=x and testX < N) and (testY >=y and testY < N):
                    if a == li[testX][testY]:
                        b = ""
                        if testX == x:
                            for j in range(M):
                                b += li[x][y + j]
                        elif testY == y:
                            for j in range(M):
                                b += li[x + j][y]
                        result = mycir(b)
                        if result:
                            result = b
                            x = N+1
                            y = N+1
                            break
            if x == N+1 and y == N+1:
                break
        if x == N+1 and y == N+1:
            break
    print(f'#{tc+1} {result}')