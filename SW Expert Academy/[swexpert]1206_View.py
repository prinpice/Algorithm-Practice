count = 0
str = ""
for i in range(10):
    count += 1
    n = int(input())
    li = list(map(int, input().split()))

    
    sum = 0
    # for i in range(2, len(li)-2):
    #     if (li[i] > li[i+1] and li[i] > li[i+2]) and (li[i] > li[i-1] and li[i] > li[i-2]):
    #         a = li[i] - li[i+2]
    #         b = li[i] - li[i+1]
    #         c = li[i] - li[i-1]
    #         d = li[i] - li[i-2]
    #         sum += min(a, b, c, d)
    # str = f'#{i+1} {sum}\n'
    # print(str)

    for i in range(2, len(li)-2):
        m = max(li[i-2], li[i-1], li[i+1], li[i+2]) 
        if  max(li[i-2], li[i-1], li[i+1], li[i+2]) < li[i]:
            sum+= li[i] - m
    str += f'#{count} {sum}\n'
print(str)