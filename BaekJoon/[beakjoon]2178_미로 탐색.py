import sys
from collections import deque
sys.setrecursionlimit(10**5)
sys.stdin = open("미로 탐색.txt", "r")

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS():
    global N, M
    if len(queuelist):
        point_y, point_x, count = queuelist.popleft()
        # print(*visited, sep="\n")
        # print("=========================")
        if point_y == N-1 and point_x == M-1:
            return count
        for d in range(4):
            new_y = point_y + dy[d]
            new_x = point_x + dx[d]
            if -1 < new_y < N and -1 < new_x < M and not visited[new_y][new_x]:
                if mirolist[new_y][new_x] == 1:
                    visited[new_y][new_x] = True
                    queuelist.append((new_y, new_x, count + 1))
        return BFS()
    return -1




N, M = map(int, input().split())
mirolist = [list(map(int, list(input()))) for _ in range(N)]
# queuelist = [(0, 0, 1)]
queuelist = deque()
queuelist.append((0, 0, 1))
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0] = True
result = BFS()
print(result)