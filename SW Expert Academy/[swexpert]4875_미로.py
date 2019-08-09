T = int(input())


for t in range(T):
    N = int(input())
    mirolist = [0] * N
    for n in range(N):
        mirolist[n] = list(map(int, (",".join(input())).split(',')))
    endpoint = list()
    dx = [0, 0, -1, 1] # 상 하 좌 우
    dy = [-1, 1, 0, 0]
    for i in range(N):
        for j in range(N):
            if mirolist[i][j] == 3:
                endpoint = [i, j]
            if mirolist[i][j] == 0:
                count = 0
                for m in range(4):
                    tempstarty = i + dy[m]
                    tempstartx = j + dx[m]
                    if (tempstarty>= 0 and tempstarty < N) and (tempstartx>= 0 and tempstartx < N):
                        if mirolist[tempstarty][tempstartx] == 0 or (mirolist[tempstarty][tempstartx] == 3 or mirolist[tempstarty][tempstartx] == 2):
                            count += 1
                if count < 2:
                    mirolist[i][j] = 1
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if mirolist[i][j] == 0:
                count = 0
                for m in range(4):
                    tempstarty = i + dy[m]
                    tempstartx = j + dx[m]
                    if (tempstarty>= 0 and tempstarty < N) and (tempstartx>= 0 and tempstartx < N):
                        if mirolist[tempstarty][tempstartx] == 0 or (mirolist[tempstarty][tempstartx] == 3 or mirolist[tempstarty][tempstartx] == 2):
                            count += 1
                if count < 2:
                    mirolist[i][j] = 1
    result = 0
    for q in range(4):
        tempstarty = endpoint[0] + dy[q]
        tempstartx = endpoint[1] + dx[q]
        if (tempstarty >= 0 and tempstarty < N) and (tempstartx >= 0 and tempstartx < N):
            if mirolist[tempstarty][tempstartx] == 0:
                result = 1
    print(f'#{t+1} {result}')