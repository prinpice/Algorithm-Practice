def dump(dm, li):
    for _ in range(dm):
        li[li.index(max(li))] -= 1
        li[li.index(min(li))] += 1
    return max(li)-min(li)

TC = 10
for i in range(TC):
    dm = int(input())
    li = list(map(int, input().split()))
    print(f'#{i+1} {dump(dm, li)}')