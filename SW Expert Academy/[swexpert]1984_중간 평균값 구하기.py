T = int(input())

for t in range(T):
    li = list(map(int, input().split()))
    sum = 0
    for i in li:
        if i > min(li) and i < max(li):
            sum += i
    avg = round(sum/(len(li)-2))
    print(f'#{t+1} {avg}')