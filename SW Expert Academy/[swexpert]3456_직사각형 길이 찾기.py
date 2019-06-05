

for t in range(int(input())):

    a, b, c = map(int, input().split())
    if a == b:
        result = c
    elif b == c:
        result = a
    elif a == c:
        result = b

    print(f'#{t+1} {result}')