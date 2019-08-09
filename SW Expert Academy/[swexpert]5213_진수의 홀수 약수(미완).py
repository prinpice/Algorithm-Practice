
T = int(input())
for a in range(T):
    sum = 0
    L, R = map(int, input().split())
    for i in range(1, R+1):
        if i % 2 != 0:
            r = (R//i)
            if i < L:
                if L % i == 0:
                    l = L // i-1
                    sum+= i * (r-l)
                    #print("A", sum)
                else:
                    l = L // i
                    sum += i * (r-l)
                    #print("C", sum)
            else:
                sum += i * r
                #print("B", sum)
        # for j in range(1, round(i**0.5)+1):
        #     if divmod(i, j)[1] == 0:
        #         b = divmod(i, j)[0]
        #         if b % 2 != 0:
        #             sum+= b
        #         if j % 2 != 0 and j != b:
        #             sum+= j
    print(f'#{a+1}', sum)