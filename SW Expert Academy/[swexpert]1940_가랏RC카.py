T = int(input())

for t in range(T):
    N = int(input())
    total_s = 0
    v = 0
    acc = 0
    for _ in range(N):
        s = input()
        if len(s) != 1:
            ud, acc = map(int, s.split())
            if ud == 2:
                acc = 0 - acc
            v += acc
            if v < 0:
                v = 0
            total_s += v
        else:
            total_s += v
    print(f'#{t+1} {total_s}')
