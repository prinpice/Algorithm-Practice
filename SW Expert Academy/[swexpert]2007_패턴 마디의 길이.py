T = int(input())

for t in range(T):
    S = input()

    k = ""
    result = 0
    for s in range(len(S)):
        if len(k) == 0:
            k += S[s]
        else:
            if S[s] != k[0]:
                k += S[s]
            else:
                if k == S[len(k):len(k)*2]:
                    result = len(k)
                else:
                    k += S[s]
    print(f'#{t+1} {result}')