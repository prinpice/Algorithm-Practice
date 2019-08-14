import sys
from collections import deque
sys.stdin = open('7576.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS():
    for d in range(4):
        tempy = nowpoint[0] + dy[d]
        tempx = nowpoint[1] + dx[d]
        if -1 < tempy < N and -1 < tempx < M and boxlist[tempy][tempx] == 0:
            boxlist[tempy][tempx] = nowpoint[2] + 1
            queuepoint.append((tempy, tempx, nowpoint[2] + 1))
    return


M, N = map(int, input().split())

boxlist = [list(map(int, input().split())) for _ in range(N)]
queuepoint = deque()
tomatocount = 0
for n in range(N):
    for m in range(M):
        if boxlist[n][m] == 1:
            queuepoint.append((n, m, 0))
        elif boxlist[n][m] == 0:
            tomatocount += 1

if tomatocount == 0:
    print(0)
else:
    while len(queuepoint) > 0:
        nowpoint = queuepoint.popleft()
        BFS()

    remain = False
    max_time = -1
    for y in range(N):
        for x in range(M):
            time = boxlist[y][x]
            if time == 0:
                max_time = -1
                remain = True
                break
            elif time != -1:
                if time > max_time:
                    max_time = time
        if remain:
            break

    print(max_time)

