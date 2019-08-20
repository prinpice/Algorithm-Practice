import sys
sys.stdin = open('10952.txt', 'r')

def DFS():
    global pointlist, N, stacklist, stackvisited
    print("stackliststart", stacklist)
    if len(stacklist) == 0:
        return
    nowpoint = stacklist.pop()
    print("point", pointlist[nowpoint])
    if pointlist[nowpoint]:
        nextpoint = pointlist[nowpoint].pop(0)
        print(nextpoint)
        if nextpoint not in stackvisited:
            stackvisited.append(nextpoint)
            stacklist.append(nextpoint)
            print("stacklist", stackvisited)
            return DFS()

        print(nextpoint)
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
    pointlist[j].append(i)
    pointlist[j].sort()

print(pointlist)
pointqueuelist = pointlist[:]

stacklist = [V]
queuelist = [(1, V)]
stackvisited = [V]
queuevisited = []
DFS()
while len(stacklist) > 0 or len(queuelist) > 0:
    print("while")
    break
    # DFS()
    # BFS()
    # print(stackvisited)



