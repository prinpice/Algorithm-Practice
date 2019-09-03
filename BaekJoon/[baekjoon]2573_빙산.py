import sys
sys.stdin = open('10952.txt', 'r')
from collections import deque

N, M = map(int, input().split())

iceberg = [list(map(int, input().split())) for _ in range(N)]
zerolist = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
num = 0
maxx = 0
maxy = 0
cou = 0
while cou < 2:
    for x in range(N):
        for y in range(M):
            if iceberg[x][y] != 0:
                if y >= maxy:
                    maxy = y+1
                if x >= maxx:
                    maxx = x + 1
                tempcount = 0
                for d in range(4):
                    tempx = x + dx[d]
                    tempy = y + dy[d]
                    if 0 <= tempx < N and 0 <= tempy < M:
                        if iceberg[tempx][tempy] == 0:
                            tempcount+= 1
                zerolist[x][y] = tempcount
    for x in range(maxx):
        for y in range(maxy):
            value = iceberg[x][y]
            if value != 0:
                iceberg[x][y] = value-zerolist[x][y]
                if iceberg[x][y] < 0:
                    iceberg[x][y] = 0

    visited = [[0 for _ in range(M)] for _ in range(N)]
    stacklist = deque()


    def test():
        count = 0
        for x in range(maxx):
            for y in range(maxy):
                if iceberg[x][y] != 0 and visited[x][y] == 0:
                    if count == 1:
                        return count + 1
                    stacklist.append([x, y])
                    visited[x][y] = 1
                    while len(stacklist) != 0:
                        nowpoint = stacklist.pop()
                        nowpointx = nowpoint[0]
                        nowpointy = nowpoint[1]
                        for d in range(4):
                            nextx = nowpointx + dx[d]
                            nexty = nowpointy + dy[d]
                            if 0 <= nextx < N and 0 <= nexty < M:
                                if visited[nextx][nexty] == 0 and iceberg[nextx][nexty] != 0:
                                    visited[nextx][nexty] = 1
                                    stacklist.append([nextx, nexty])
                    count += 1
                # if count > 1:
                #     return count
        return 0
    cou = test()
    num += 1

print(num)