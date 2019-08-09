import sys
sys.stdin = open("5209.txt", "r")


def backtracking(n_sum, count):
    global MIN_VALUE
    # print(n_sum, count, MIN_VALUE)
    if count == N:
        if n_sum < MIN_VALUE or MIN_VALUE == -1:
            MIN_VALUE = n_sum
            return
    for sec_num in range(N):
        # print(count, sec_num, visited, n_sum)
        if visited[sec_num] == 0:
            # print(sec_num, visited)
            if MIN_VALUE == -1 or MIN_VALUE > n_sum + nlist[count][sec_num]:
                visited[sec_num] = 1
                n_sum += nlist[count][sec_num]
                backtracking(n_sum, count + 1)
                visited[sec_num] = 0
                n_sum -= nlist[count][sec_num]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    nlist = [list(map(int, input().split())) for _ in range(N)]
    MIN_VALUE = -1
    for num in range(N):
        visited = [0 for _ in range(N)]
        if MIN_VALUE > 0 and MIN_VALUE <=nlist[0][num]:
            continue
        visited[num] = 1
        n_sum = nlist[0][num]
        # print("n_sum", n_sum)
        backtracking(n_sum, 1)

    print(f"#{t} {MIN_VALUE}")