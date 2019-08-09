TC = int(input())

for c in range(TC):

    n = int(input())
    ai = list(map(int, input().split()))
    for i in range(len(ai)-1):
        if i % 2 == 0:
            a = max(ai[i+1:])
            if a > ai[i]:
                j = 0
                for m in range(i+1, len(ai)):
                    if ai[m] == a:
                        j = m
                ai[i], ai[j] = ai[j], ai[i]
        else:
            a = min(ai[i+1:])
            if a < ai[i]:
                j = 0
                for m in range(i+1, len(ai)):
                    if ai[m] == a:
                        j = m
                ai[i], ai[j] = ai[j], ai[i]

    print(f'#{c+1}', " ".join(list(map(str, ai[:10]))))