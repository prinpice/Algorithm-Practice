T = int(input())

for t in range(T):
    N = int(input())

    total = 0
    for n in range(N+1):
        if n %2 == 0:
            total -= n
        elif n % 2 != 0:
            total += n

    print(f'#{t+1} {total}')
