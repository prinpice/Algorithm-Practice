T = int(input())

for t in range(T):
    condlist = list(map(int, input().split()))

    nlist = [0] * (condlist[0]+1)
    for _ in range(condlist[1]):
        temp1, temp2 = map(int, input().split())
        nlist[temp1] = temp2
    if condlist[0] % 2 == 0:
        start = condlist[0]
    else:
        start = condlist[0]-1
    for re in range(start, 0, -2):
        if re == condlist[0]:
            nlist[re//2] = nlist[re]
        else:
            nlist[re//2] = nlist[re] + nlist[re+1]
    print('#{} {}'.format(t+1, nlist[condlist[2]]))



