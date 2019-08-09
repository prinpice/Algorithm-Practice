import sys
sys.stdin = open("최적 경로.txt", "r")



T = int(input())

for t in range(1, T+1):
    N = int(input())
    templist = list(map(int, input().split()))
    company = tuple(templist[:2])
    home = tuple(templist[2:4])
    customers = []
    for temp in range(4, len(templist), 2):
        customers.append((templist[temp], templist[temp+1]))
    customers.insert(0, company)
    customers.append(home)
    distance = [[0 for _ in range(N+2)] for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            distance[i][j] = abs(customers[i][0]-customers[j][0]) + abs(customers[i][1]-customers[j][1])
    print(*distance, sep="\n")

    


