
T = int(input())
for t in range(T):
    s = input()
    H = int(input())
    p_li = list(map(int, input().split()))
    for i in range(len(s), -1, -1):
        s = s[:i]+'-'*p_li.count(i)+ s[i:]
    print(f'#{t+1} {s}')