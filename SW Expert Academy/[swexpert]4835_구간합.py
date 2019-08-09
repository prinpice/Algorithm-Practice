TC = int(input())

for j in range(TC):
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))

    li = [sum(ai[i:i+m]) for i in range(0, len(ai)-m+1)]
    print(f'#{j+1}', max(li)-min(li))