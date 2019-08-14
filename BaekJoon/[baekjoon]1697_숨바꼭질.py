import sys
sys.stdin = open("숨바꼭질.txt", "r")

def BFS():
    global K
    point_now, time = queuelist.pop(0)
    if point_now == K:
        return time
    if point_now+1 not in visited:
        visited.append(point_now+1)
        queuelist.append((point_now+1, time+1))
    if point_now*2 not in visited:
        visited.append(point_now*2)
        queuelist.append((point_now*2, time+1))
    if point_now-1 not in visited:
        visited.append(point_now-1)
        queuelist.append((point_now-1, time+1))

    return BFS()

N, K = map(int, input().split())
queuelist = [(N, 0)]
visited= [N]
result = BFS()
print(result)
