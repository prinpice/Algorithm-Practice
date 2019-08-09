T = int(input())

for t in range(T):
    N, startnode = map(int, input().split())
    nlist = list(map(int, input().split()))
    nodelist = [[] for _ in range(101)]
    for n in range(0, N, 2):
        nodelist[nlist[n]].append(nlist[n+1])
    Queue = list()
    visited = list()
    num = 1
    for node in nodelist[startnode]:
        Queue.append([node, num])
        visited.append(node)
    rear = -1
    while True:
        rear += 1
        temp = Queue[rear]
        if nodelist[temp[0]] != []:
            for subnode in nodelist[temp[0]]:
                Queue.append([subnode, temp[1]])
                visited.append(subnode)
        else:
            if rear == len(Queue)-1:
                break

    maxi = Queue[-1]
    for ma in Queue:
        if ma[1] == maxi[1] and ma[0] > maxi[0]:
            maxi = ma
    print(maxi[0])

