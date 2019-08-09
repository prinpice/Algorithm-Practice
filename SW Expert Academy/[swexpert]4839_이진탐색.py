def binarySearch(p, ps):
    l = 1
    r = p
    counta = 0
    while True:
        c = int((l + r)/2)
        counta += 1
        if c == ps:
            return counta
        elif c > ps:
            r = c
        else:
            l = c



TC = int(input())

for c in range(TC):

    p, pa, pb = map(int, input().split())

    ca = binarySearch(p, pa)
    cb = binarySearch(p, pb)
    if ca > cb:
        print(f'#{c+1} B')
    elif ca < cb:
        print(f'#{c+1} A')
    else:
        print(f'#{c+1} 0')