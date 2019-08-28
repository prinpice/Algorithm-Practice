import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for t in range(int(input())):

    N = int(input())
    miro_list = [list(map(int, list(input()))) for _ in range(N)]
    start = ()
    end = ()
    queue_list = deque()
    visited = []
    for idx1 in range(N):
        for idx2 in range(N):
            if miro_list[idx1][idx2] == 2:                
                start = (idx1, idx2)
            if miro_list[idx1][idx2] == 3:
                end = (idx1, idx2)
    count = 1
    while True:

        for d in range(4):
            tempx = start[0] + dx[d]
            tempy = start[1] + dy[d]
            if (0 <= tempx < N and 0 <= tempy < N) and (tempx, tempy) not in visited:       
                if miro_list[tempx][tempy] == 0 or miro_list[tempx][tempy] == 3:
                    queue_list.appendleft(((tempx, tempy), count))
                    visited.append((tempx, tempy))
        if len(queue_list) == 0:
            print("#{} {}".format(t+1, 0))
            break
        sub = queue_list.pop()
        start, count = sub[0], sub[1]
        if start == end:
            print("#{} {}".format(t+1, count-1))
            break
        count += 1
        


