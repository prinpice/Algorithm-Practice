TC = int(input())

for i in range(TC):
    n = int(input())
    ai = list(map(int, input().split()))
    print(f'#{i+1} {max(ai) - min(ai)}')