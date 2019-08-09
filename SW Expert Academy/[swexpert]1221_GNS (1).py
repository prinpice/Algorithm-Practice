TC = int(input())

for tc in range(TC):

    n, m = map(str, input().split())
    m = int(m)
    s = input()
    li = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a = ""
    for i in range(len(s)):
        if s[i] != " ":
            a += s[i] 
            print(s[i])
            print(a)
        else:
            if a == 'ZRO':
                li[0] += 1
            elif a == 'ONE':
                li[1] += 1
            elif a == 'TWO':
                li[2] += 1
            elif a == 'THR':
                li[3] += 1
            elif a == 'FOR':
                li[4] += 1
            elif a == 'FIV':
                li[5] += 1
            elif a == 'SIX':
                li[6] += 1
            elif a == 'SVN':
                li[7] += 1
            elif a == 'EGT':
                li[8] += 1
            elif a == 'NIN':
                li[9] += 1
            a = ""
    print(n)
    li_week = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for j in range(len(li)):
        for k in range(li[j]):
            print(li_week[j], end=" ")
    print()
    