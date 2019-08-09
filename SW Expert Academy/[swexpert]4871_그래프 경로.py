def finda(s, g, li, re):

    for n in range(len(li)):
        if li[n][0] == s:
            if li[n][1] == g:
                re = 1
            else:
                re = finda(li[n][1], g, li, re)
    return re


T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    li = [0] * E
    for e in range(E):
        li[e] = list(map(int, input().split()))
    S, G = map(int, input().split())
    re = 0
    result = finda(S, G, li, re)

    print('#{} {}'.format(t + 1, result))