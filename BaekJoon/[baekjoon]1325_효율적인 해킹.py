"""

1. visited 를 append 로 쓰지 않는다.
    visited[new_computer] = True -> 방문불가
    visited[new_computer] = False -> 방문가능

2. 중복된 점을 탐색하지말자.

"""



import sys
sys.stdin = open("효율적인 해킹.txt", "r")
sys.setrecursionlimit(10**5)

def DFS():
    if len(stacklist) == 0:
        return
    now = stacklist.pop()
    for ml in mlist[now]:
        if not visited[ml]:
            will_go[ml] = 1
            visited[ml] = 1
            stacklist.append(ml)
    return DFS()


N, M = map(int, input().split())
mlist = [[] for _ in range(N+1)]
for _ in range(M):
    b, a = map(int, input().split())
    mlist[a].append(b)

countlist = [0 for _ in range(N+1)]
will_go = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if not will_go[i]:
        stacklist = [i]
        visited = [0 for _ in range(N+1)]
        visited[i] = 1
        DFS()
        countlist[i] = sum(visited)

maxnum = max(countlist)
for j in range(1, N+1):
    if countlist[j] == maxnum:
        print(str(j), end=" ")