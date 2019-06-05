T = int(input())

for t in range(T):
    s = input()
    pas = s[::-1]
    result = 0
    if s == pas:
        result = 1
    print(f'#{t+1} {result}')