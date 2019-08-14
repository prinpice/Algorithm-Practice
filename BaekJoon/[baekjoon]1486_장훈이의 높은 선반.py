import sys
sys.stdin = open("장훈이의 높은 선반.txt", "r")


T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    nlist = list(map(int, input().split()))
    A_size = len(nlist)
    MIN_VALUE = -1
    for i in range(2**A_size):
        flag = bin(i)[2:].zfill(A_size)
        subset = [nlist[j] for j in range(A_size) if flag[j] == '1']
        if sum(subset) >= B:
            if MIN_VALUE == -1 or MIN_VALUE > abs(sum(subset)-B):
                MIN_VALUE = abs(sum(subset)-B)
    print(f"#{t} {MIN_VALUE}")
