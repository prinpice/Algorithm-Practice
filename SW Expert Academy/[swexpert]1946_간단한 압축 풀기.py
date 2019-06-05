T = int(input())

for t in range(T):

    
    N = int(input())

    print(f'#{t+1}')
    s = ""
    for n in range(N):
        al, num = input().split()

        for _ in range(int(num)):
            if len(s) < 10:
                s += al
                # print('s', s)
            else:
                # s_li.append(s)
                # s = al
                print(s)
                s = al
    print(s)
