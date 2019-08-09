import sys
sys.stdin = open("5247.txt", "r")

from collections import deque

def BFS():
    global result, M
    if len(queuelist) == 0:
        return
    now, count = queuelist.popleft()

    if (now + 1) not in visited:
        if now + 1 == M:
            result = count+1
            return
        visited.append(now+1)
        queuelist.append((now+1, count+1))
    if (now - 1) not in visited:
        if now - 1 == M:
            result = count+1
            return
        visited.append(now-1)
        queuelist.append((now-1, count+1))
    if (now * 2) not in visited:
        if now * 2 == M:
            result = count+1
            return
        visited.append(now*2)
        queuelist.append((now*2, count+1))
    if (now - 10) not in visited:
        if now - 10 == M:
            result = count+1
            return
        visited.append(now - 10)
        queuelist.append((now-10, count+1))
    BFS()

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    visited = [N]
    queuelist = deque()
    queuelist.append((N, 0))
    result = 0
    BFS()
    print(f"#{t} {result}")
