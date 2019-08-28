
for t in range(int(input())):
    N, M = map(int, input().split())
    idx = M % N
    queuelist = list(map(int, input().split()))
    print("#{} {}".format(t+1, queuelist[idx]))