TC = int(input())

for tc in range(TC):

    str1 = input()
    str2 = input()

    li = []

    for i in range(len(str1)):
        count = 0
        for j in range(len(li)):
            if li[j] == str1[i]:
                count += 1
                break
        if count == 0:
            li += str1[i]

    count_li = [0] * len(li)
    for k in range(len(str2)):
        for n in range(len(li)):
            if str2[k] == li[n]:
                count_li[n] += 1

    maxi = count_li[0]
    for t in range(len(count_li)):
        if maxi < count_li[t]:
            maxi = count_li[t]
    print(f'#{tc+1} {maxi}')