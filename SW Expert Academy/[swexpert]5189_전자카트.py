import sys
sys.stdin = open("5189.txt", "r")


import itertools

def findsum(nodeorder):
    MIN_VALUE = -1
    # print(nodeorder)
    for nodeor in nodeorder:
        # print(nodeor)
        tempsum = nlist[0][nodeor[0]-1]
        for num in range(len(nodeor)-1):
            tempsum += nlist[nodeor[num]-1][nodeor[num+1]-1]
        tempsum += nlist[nodeor[-1]-1][0]
        if MIN_VALUE == -1:
            MIN_VALUE = tempsum
        elif MIN_VALUE > tempsum:
            MIN_VALUE = tempsum
    return MIN_VALUE

T = int(input())

for t in range(1, T+1):
    N = int(input())
    nlist = [list(map(int, input().split())) for _ in range(N)]
    nl = list(range(2, N+1))
    result = 0
    perm = itertools.permutations(nl)
    result = findsum(perm)
    print(f"#{t} {result}")


print(tuple([1]))