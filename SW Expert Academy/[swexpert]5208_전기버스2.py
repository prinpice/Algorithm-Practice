import sys
sys.stdin = open("5208.txt", "r")
T = int(input())

for t in range(T):
    busstop = list(map(int, input().split()))
    N = busstop.pop(0)
    busstop.append(0)
    countlist = [0 for _ in range(N)]
    for idx in range(N-2, -1, -1):
        for num in range(1, busstop[idx]+1):
            if idx+num < N and countlist[idx] > 1+countlist[idx+num] or countlist[idx] == 0:
                countlist[idx] = 1+countlist[idx+num]
    print(f"#{t+1} {countlist[0]-1}")

