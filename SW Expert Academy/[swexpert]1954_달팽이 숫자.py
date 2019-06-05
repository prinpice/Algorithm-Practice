TC = int(input())

for tc in range(TC):
    N = int(input())

    li = [[0] * N for _ in range(N)]

    dx = 0
    dy = 1

    x, y = 0, 0

    for i in range(N**2):
        li[x][y] = i+1
        if dy == 1:
            if y+dy < N and li[x][y+dy] == 0:
                y += dy
            else:
                dy = 0
                dx = 1
                x += dx
        elif dx == 1:
            if x+dx < N and li[x+dx][y] == 0:
                x += dx
            else:
                dx = 0
                dy = -1
                y += dy
        elif dy == -1:
            if y+dy > -1 and li[x][y+dy] == 0:
                y += dy
            else:
                dy = 0
                dx = -1
                x += dx
        elif dx == -1:
            if x+dx > -1 and li[x+dx][y] == 0:
                x += dx
            else:
                dx = 0
                dy = 1
                y += dy
    print(f'#{tc+1}')
    for m in range(N):
        for n in range(N):
            print(li[m][n], end=" ")
        print()

        
    