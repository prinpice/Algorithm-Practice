import sys
sys.stdin = open("10952.txt", "r")

from collections import deque

N, K = map(int, input().split())
answer = 0
k = K * 2
visited = []

queue = deque()

queue.appendleft((0, N))
visited.append(N)

while len(queue) > 0:
    idx, number = queue.pop()
    cal1 = number * 2
    cal2 = number + 1
    cal3 = number - 1
    if cal1 == K or (cal2 == K or cal3 == K):
        answer = idx + 1
        break
    if cal1 < k and cal1 not in visited:
        visited.append(cal1)
        queue.appendleft((idx + 1, cal1))
    if cal2 not in visited:
        visited.append(cal2)
        queue.appendleft((idx + 1, cal2))
    if cal3 >= 0 and cal3 not in visited:
        visited.append(cal3)
        queue.appendleft((idx + 1, cal3))
print(answer)