import sys
sys.stdin = open('1260.txt', 'r')

def DFS():
    global pointlist, N, stacklist, stackvisited
    if not stacklist:
        return
    nowpoint = stacklist.pop()
    print("point", pointlist[nowpoint])
    if pointlist[nowpoint]:
        nextpoint = pointlist[nowpoint].pop(0)
        if nextpoint not in stackvisited:
            stackvisited.append(nextpoint)
            stacklist.append(nextpoint)
            print(stackvisited)
            return DFS()
    return

def BFS():
    global pointqueuelist, N, queuelist, queuevisited
    return



N, M, V = map(int, input().split())
pointlist = [list() for _ in range(N+1)]
for m in range(M):
    i, j = map(int, input().split())
    pointlist[i].append(j)
    pointlist[i].sort()

print(pointlist)
pointqueuelist = pointlist[:]

stacklist = [V]
queuelist = [(1, V)]
stackvisited = [V]
queuevisited = []
while len(stacklist) > 0 or len(queuelist) > 0:
    DFS()
    BFS()
    # print(stackvisited)



