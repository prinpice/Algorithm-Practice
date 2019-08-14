import sys
sys.stdin = open("적록색약.txt", "r")
from copy import deepcopy


N = int(input())
colorlist = [list(input()) for _ in range(N)]
colorlist1 = [["" for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if colorlist[i][j] == 'R' or colorlist[i][j] == 'G':
            colorlist1[i][j] = 'R'
        else:
            colorlist1[i][j] = colorlist[i][j]
visited = [[False for _ in range(N)] for _ in range(N)]
visited1 = deepcopy(visited)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
count1 = 0
count2 = 0

def DFS1(i, j, color):

    for d in range(4):
        now_i = dy[d] + i
        now_j = dx[d] + j
        if 0 <= now_i <N and 0 <=now_j < N and not visited[now_i][now_j] and color == colorlist[now_i][now_j]:
            visited[now_i][now_j] = True
            DFS1(now_i, now_j, color)

def DFS2(i, j, color):
    for d in range(4):
        now_i = dy[d] + i
        now_j = dx[d] + j
        if 0 <= now_i <N and 0 <=now_j < N and not visited1[now_i][now_j] and color == colorlist1[now_i][now_j]:
            visited1[now_i][now_j] = True
            DFS2(now_i, now_j, color)

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS1(i, j, colorlist[i][j])
            count1 += 1
        if not visited1[i][j]:
            DFS2(i, j, colorlist1[i][j])
            count2 += 1

print(count1, count2)





