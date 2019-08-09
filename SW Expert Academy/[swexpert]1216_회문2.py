def palicol(b):
    if len(b) == 0 or len(b) == 1:
        return True
    else:
        if b[0] == b[len(b)-1]:
            dc = ""
            for q in range(1, len(b)-1):
                dc += b[q]
            return palicol(dc)
        else:
            return False



TC = 10
for tc in range(TC):
    ct = int(input())
    li = ["" for _ in range(100)]
    for idx in range(100):
        c = input()
        li[idx] = c


    leng = 0
    for i in range(100):
        for j in range(100):
            for k in range(99, j-1, -1):
                s = ""
                if li[i][j] == li[i][k]:
                    for t in range(j, k+1):
                        s += li[i][t]
                    st = s
                    result = palicol(s)
                    if result:
                        if leng < len(st):
                            leng = len(st)
            for k in range(99, i-1, -1):
                s = ""
                if li[i][j] == li[k][j]:
                    for t in range(i, k+1):
                        s += li[t][j]
                    st = s
                    result = palicol(s)
                    if result:
                        if leng < len(st):
                            leng = len(st)
    print(f'#{ct} {leng}')
