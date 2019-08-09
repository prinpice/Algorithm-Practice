TC = int(input())

for i in range(TC):
    n = int(input())
    ai = list(input())

    dic = {int(c): ai.count(c) for c in set(ai)}
    li = [key for key, val in dic.items() if val == max(dic.values())]
    re = li[0]
    if sum(value == dic[re] for value in dic.values()) > 1:
        re = max(li)
    print(f'#{i+1} {re}', dic[re])