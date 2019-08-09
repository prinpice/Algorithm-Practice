import sys
sys.stdin = open('savegard.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def DFS(number):
    global visited, nlist, N, stacklist
    nowpoint = stacklist.pop()
    y = nowpoint[0]
    x = nowpoint[1]

    for d in range(4):
        tempy = y + dy[d]
        tempx = x + dx[d]
        if -1 < tempy < N and -1 < tempx < N and not visited[tempy][tempx]:
            if nlist[tempy][tempx] > number:
                # print("step",[tempy, tempx])
                visited[tempy][tempx] = True
                stacklist.append([tempy, tempx])

    # print(stacklist)
    return

N = int(input())

nlist = [list(map(int, input().split())) for _ in range(N)]
nlistset = set()
for n in range(N):
    nlistset.update(nlist[n])
# print(nlistset)
nlistset.remove(max(nlistset))
# numberlist= list(nlistset)
# numberlist.reverse()
# numberlist = numberlist[1:]
maxnumber = 1
for number in nlistset:
    visited = [[False for _ in range(N)] for _ in range(N)]
    stacklist = []
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if nlist[i][j] > number:
                    visited[i][j] = True
                    stacklist.append([i, j])
                    while len(stacklist) > 0:
                        DFS(number)
                    count += 1

    if count > maxnumber:
        maxnumber = count
print(maxnumber)
