def compare(comlist):
    relist = list()
    for compindex in range(0, len(comlist)-1, 2):
        if comlist[compindex][1] == 1:
            if comlist[compindex+1][1] == 1 or comlist[compindex+1][1] == 3:
                relist.append(comlist[compindex])
            elif comlist[compindex+1][1] == 2:
                relist.append(comlist[compindex+1])
    if len(relist) == 1:
        return relist[0]
    else:
        return compare(relist)

T = int(input())

for t in range(T):
    N = int(input())
    startlist = list(map(int, input().split()))
    for m in range(len(startlist)):
        startlist[m] = [m+1, startlist[m]]
    firstlist = startlist[:N//2+1]
    secondlist = startlist[N//2+1:]
    result = compare(compare(firstlist)+compare(secondlist))
    print(f'#{t+1} {result[0]}')
    

