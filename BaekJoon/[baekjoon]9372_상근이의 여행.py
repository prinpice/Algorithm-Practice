import sys
sys.stdin = open("상근이의 여행.txt", "r")

def BFS():
    

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    planelist = list()
    for _ in range(M):
        planelist.append(tuple(input().split()))
    queuelist = []
    visited = [False for _ in range(M)]



    print(planelist)

