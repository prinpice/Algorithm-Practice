T = int(input())

for t in range(T):
    total_list = [0, 0, 0, 0, 0]
    N = int(input())
    while N != 1:
        if N % 2 == 0:
            total_list[0] += 1
            N = N // 2
        if N % 3 == 0: 
            total_list[1] += 1
            N = N // 3
        if N % 5 == 0:
            total_list[2] += 1
            N = N // 5
        if N % 7 == 0:
            total_list[3] += 1
            N = N // 7
        if N % 11 == 0:
            total_list[4] += 1
            N = N // 11
    print(f'#{t+1} {" ".join(map(str, total_list))}')