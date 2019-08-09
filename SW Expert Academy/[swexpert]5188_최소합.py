import sys
sys.stdin = open("5188.txt", "r")
move_i = [1, 0]
move_j = [0, 1]


def dfs(i, j, val):
    valuelist = [(i, j, val)]
    MIN_VALUE = -1

    while len(valuelist):
        ci, cj, cval = valuelist.pop(0)

        if ci == N-1 and cj == N-1:
            if MIN_VALUE == -1:
                MIN_VALUE = cval
            elif MIN_VALUE > cval:
                MIN_VALUE = cval

        for d in range(2):
            new_i = ci + move_i[d]
            new_j = cj + move_j[d]
            if new_i <N and new_j < N and (new_i, new_j, cval+nlist[new_i][new_j]) not in valuelist:
                valuelist.append((new_i, new_j, cval+nlist[new_i][new_j]))
    return MIN_VALUE


T = int(input())

for t in range(1, T+1):
    N = int(input())

    nlist = [list(map(int, input().split())) for _ in range(N)]
    result = dfs(0, 0, nlist[0][0])


    print(f"#{t} {result}")