def finda(s_li):
    for n in range(len(s_li)-1):
        if s_li[n] == s_li[n+1]:
            t_li = [""]*(len(s_li)-2)
            for i in range(0, n):
                t_li[i] = s_li[i]
            for j in range(n+2, len(s_li)):
                t_li[j-2] = s_li[j]
            return finda(t_li)
    return len(s_li)

T = int(input())

for t in range(T):
    s_li = list(input())
    le = finda(s_li)
    print('#{} {}'.format(t+1, le))