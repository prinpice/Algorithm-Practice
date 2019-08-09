
for t in range(int(input())):

    A, B, C = map(int, input().split())
    if A >= B:
        result = C // B
    else:
        result = C // A


    print(f'#{t+1} {result}')