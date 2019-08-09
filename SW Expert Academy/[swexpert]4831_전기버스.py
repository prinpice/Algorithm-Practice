TC = int(input())


for j in range(TC):
    k, n, m = map(int, input().split())
    li_m = list(map(int, input().split()))

    count, pl = 0, 0
    for i in range(len(li_m)-1):
        if li_m[i+1]-li_m[i] > k:
            pl = n
    while pl < n:
        for i in range(k, 0, -1):
            if (pl + i) in li_m:
                count += 1
                pl += i
                break
            if (pl + i) >= n:
                pl = n
                break
    print(f'#{j+1}', count)