
T = int(input())
for i in range(T):
    tc = int(input())
    li = list(map(int, input().split()))
    dic = {int(c): li.count(c) for c in set(li)}
    re = [key for key, val in dic.items() if val == max(dic.values())][0]
    if sum(value == re for value in dic.values()) > 1:
        re = max(dic.keys())
    print(f'#{tc} {re}')