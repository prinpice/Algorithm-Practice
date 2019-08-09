def totalcal(li):
    if len(li) > 2:
        t3 = templist.pop()
        t2 = templist.pop()
        t1 = templist.pop()
        telist = [t1, t2, t3]

        return calculation(telist)
    else:
        return 'error'


def calculation(li):
    result = 0
    if '.' in li:
        return 'error'
    else:
        if li[2] == '+':
            result = int(li[0]) + int(li[1])
        elif li[2] == '/':
            result = int(li[0]) // int(li[1])
        elif li[2] == '*':
            result = int(li[0]) * int(li[1])
        elif li[2] == '-':
            result = int(li[0]) - int(li[1])
    return result

T = int(input())

for t in range(T):

    stacklist = list(input().split())
    ind = stacklist.index('.')
    stacklist = stacklist[:ind]
    stacklist = stacklist[::-1]

    templist = list()
    total = 0
    while True:
        if len(stacklist) == 0:
            if len(templist) == 1:
                total = templist[0]
            else:
                total = 'error'
            break
        temp = stacklist.pop()


        if temp not in ['+', '/', '-', '*']:
            templist.append(int(temp))

        elif temp in ['+', '/', '-', '*']:
            templist.append(temp)
            tempa = totalcal(templist)
            if tempa == 'error':
                total = tempa
                break
            else:
                stacklist.append(tempa)


    print(f"#{t+1} {total}")

