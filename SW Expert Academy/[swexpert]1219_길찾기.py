import sys
sys.stdin = open("1219.txt", "r")

def DFS():
    global result
    # print(*visited)
    if 99 in visited:
        result = 1
        return
    if not len(stacklist):
        return
    now = stacklist.pop()
    if now == 99:
        result = 1
        return
    if len(nodelist[now]):
        for node in nodelist[now]:
            visited.append(node)
            stacklist.append(node)




for _ in range(10):
    t, N = map(int, input().split())
    templist = list(map(int, input().split()))
    nodelist = [[] for _ in range(100)]
    for n in range(0, N*2, 2):
        nodelist[templist[n]].append(templist[n+1])
    # print(*nodelist, sep="\n")
    result = 0
    visited = [0]
    stacklist = [0]
    while result == 0 and len(stacklist):
        DFS()
    print(result)


