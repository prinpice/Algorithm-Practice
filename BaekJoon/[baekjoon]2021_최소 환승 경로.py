import sys
sys.stdin = open("최소 환승 경로.txt", "r")



N, L = map(int, input().split())
placelist = [[] for _ in range(N+1)]
linelist = [list(map(int, input().split())) for _ in range(L)]
for line in linelist:
    line.remove(-1)
print(linelist)

start, end = map(int, input().split())



