N = int(input())
graph = []
for _ in range(N):
    graph.append([])

for i in range(N):
    temp_list = list(map(int, input().split()))
    for j, val in enumerate(temp_list):
        if val == 1:
            graph[i].append(j)
            graph[j].append(i)
print(graph)