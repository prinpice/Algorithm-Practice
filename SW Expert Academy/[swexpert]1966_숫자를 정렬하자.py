
T = int(input())
for t in range(T):
    N = int(input())
    s_li = list(map(int, input().split()))
    s_li.sort()
    s = ""
    for i in range(len(s_li)):
        s += str(s_li[i]) + " "
    print(f'#{t+1} {s}')
