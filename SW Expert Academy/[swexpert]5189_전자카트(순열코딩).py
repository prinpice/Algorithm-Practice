import sys

sys.stdin = open("5189.txt","r")

for tc in range(1,int(input())+1):
    n = int(input())
    office = [list(map(int,input().split())) for _ in range(n)]
    is_visited = [0 for _ in range(n)]
    is_visited[0] = 1
    min_res = sum(map(sum,office))
    def brute_force(curr,res,cnt):
        print(is_visited)
        global min_res
        if cnt == n-1:
            if min_res > res+office[curr][0]:
                min_res = res+office[curr][0]
            return

        if res > min_res:
            return

        for idx in range(n):
            if idx != curr and is_visited[idx] == 0:
                # print(" ", idx, is_visited)
                is_visited[idx] = 1
                brute_force(idx,res+office[curr][idx],cnt+1)
                is_visited[idx] = 0

    for idx in range(1,n):
        # is_visited[idx] = 1
        # print(idx, is_visited)
        is_visited[idx] = 0
        print(idx, office[0][idx])
        brute_force(idx,office[0][idx],1)
    print(f"#{tc} {min_res}")