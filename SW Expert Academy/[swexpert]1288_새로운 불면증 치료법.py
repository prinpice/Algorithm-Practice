T = int(input())

for t in range(T):
    N = int(input())
    nlist = list()
    count = 0
    while len(nlist) != 10:
        ntemp = (count+1) * N
        while ntemp != 0:
            nrest = ntemp%10
            ntemp = ntemp//10
            if nrest not in nlist:
                nlist.append(nrest)
        count += 1
    print(f'#{t+1} {count*N}')
    print(nlist)
