import sys
sys.stdin = open("1217.txt", "r")

def recursive(N, M):

    if M == 1:
        return N
    return N * recursive(N, M-1)



for _ in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    result = recursive(N, M)
    print(f"#{T} {result}")

