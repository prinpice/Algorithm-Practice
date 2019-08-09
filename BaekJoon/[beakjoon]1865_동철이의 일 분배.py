import sys
sys.stdin = open("동철이의 일 분배.txt", "r")

def backtracking(n_mul, count):
    global MAX_VALUE
    if count == N:
        if n_mul > MAX_VALUE or MAX_VALUE == 0:
            MAX_VALUE = n_mul
            return
    for sec_num in range(N):
        if not visited[sec_num]:
            temp = nlist[count][sec_num]*0.01
            if MAX_VALUE < n_mul * temp:
                visited[sec_num] = 1
                backtracking(n_mul*temp, count + 1)
                visited[sec_num] = 0

T = int(input())

for t in range(1, T+1):
    N = int(input())
    nlist = [list(map(int, input().split())) for _ in range(N)]
    MAX_VALUE = 0
    for num in range(N):
        visited = [0 for _ in range(N)]
        if MAX_VALUE >= nlist[0][num]:
            continue
        visited[num] = 1
        n_mul = nlist[0][num]*0.01
        backtracking(n_mul, 1)
    MAX_VALUE *= 100
    print(f"#{t} {'%0.6f' %MAX_VALUE}")
