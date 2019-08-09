T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    nodelist = [[0] for _ in range(V+1)]
    for _ in range(V):
        temp0, temp1 = map(int, input().split())
        nodelist[temp0].append(temp1)
    print(nodelist)