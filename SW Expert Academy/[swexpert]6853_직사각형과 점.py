
T = int(input())

for t in range(T):
    X1, Y1, X2, Y2 = map(int, input().split())
    result_li = [0, 0, 0]
    N = int(input())
    for n in range(N):
        x, y = map(int, input().split())
        if (x > X1 and x < X2) and (y > Y1 and y < Y2):
            result_li[0] += 1
        elif (x < X1 or x > X2) or (y < Y1 or y > Y2):
            result_li[2] += 1
        else:
            result_li[1] += 1

    print('#{} {} {} {}'.format(t+1, result_li[0], result_li[1], result_li[2]))
