import sys
sys.stdin = open('secret_code.txt', 'r')

secret_code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    nlist = [input() for _ in range(N)]

    str = ""

    for nstring in nlist:
        if "1" in nstring:
            str = nstring
            break


    for i in range(M-1, -1, -1):
        if str[i] == '1':
            str = str[i-55:i+1]
            break
    strlist = []
    while len(str) > 0:
        strlist.append(str[0: 7])
        str = str[7:]

    numlist = [0, ]
    for strli in strlist:
        numlist.append(secret_code.index(strli))

    numsum = 0
    oddsum = 0
    result = 0
    for numidx in range(len(numlist)):
        if numidx % 2 == 0:
            numsum += numlist[numidx]
        else:
            oddsum += numlist[numidx]
        result += numlist[numidx]


    numsum += (oddsum*3)

    if numsum % 10 == 0:
        print(f'#{t+1} {result}')
    else:
        print(f'#{t+1} {0}')
