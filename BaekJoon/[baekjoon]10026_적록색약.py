import sys
import time
sys.stdin = open('10952.txt', 'r')
start = time.time()

N = int(input())
colorlist = [list(input()) for _ in range(N)]

visited1 = [[0 for _ in range(N)] for _ in range(N)]
visited2 = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count1 = 0
color1 = ''
count2 = 0
color2 = ''

stacklist1 = []
stacklist2 = []

visited1[0][0] = 1
visited2[0][0] = 1

stacklist1.append([0, 0])
stacklist2.append([0, 0])

color1 = colorlist[0][0]
color2 = colorlist[0][0]

while len(stacklist1) != 0:
    # R != G
    while True:
        nowpoint = stacklist1.pop(0)
        x = nowpoint[0]
        y = nowpoint[1]
        for d in range(4):
            if 0 <= x + dx[d] < N and 0 <= y + dy[d] < N:
                testx = x+dx[d]
                testy = y+dy[d]
                if visited1[testx][testy] == 0 and colorlist[testx][testy] == color1:
                    stacklist1.append([testx, testy])
                    visited1[testx][testy] = 1
        if len(stacklist1) == 0:
            count1 += 1
            break

    for pointx in range(N):
        for pointy in range(N):
            if visited1[pointx][pointy] == 0:
                stacklist1.append([pointx, pointy])
                visited1[pointx][pointy] = 1
                color1 = colorlist[pointx][pointy]
                break
        if len(stacklist1) != 0:
            break

for i in range(N):
    for j in range(N):
        if colorlist[i][j] == 'G':
            colorlist[i][j] = 'R'
if color2 == 'G':
    color2 = 'R'

while len(stacklist2):
    # R == G
    while True:
        nowpoint = stacklist2.pop(0)
        x = nowpoint[0]
        y = nowpoint[1]
        for d in range(4):
            if 0 <= x + dx[d] < N and 0 <= y + dy[d] < N:
                nextx = x + dx[d]
                nexty = y + dy[d]
                if visited2[nextx][nexty] == 0 and colorlist[nextx][nexty] == color2:
                    stacklist2.append([nextx, nexty])
                    visited2[nextx][nexty] = 1
        if len(stacklist2) == 0:
            count2 += 1
            break
    
    for pointx in range(N):
        for pointy in range(N):
            if visited2[pointx][pointy] == 0:
                stacklist2.append([pointx, pointy])
                visited2[pointx][pointy] = 1
                color2 = colorlist[pointx][pointy]
                break
        if len(stacklist2) != 0:
            break
                
print(count1, count2)
# print("time: ", time.time()-start)

