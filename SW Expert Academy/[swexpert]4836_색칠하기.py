TC = int(input())

for c in range(TC):

    li = [[0 for i in range(10)] for j in range(10)]
    N = int(input())
    for n in range(N):

        r1, c1, r2, c2, co = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if li[i][j] != 3:
                    li[i][j] += co
    counti = 0
    for i in range(len(li)):
        counti +=li[i].count(3)
    print(f'#{c+1}', counti)