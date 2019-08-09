import sys
sys.stdin = open('4881.txt', 'r')


def totalcal(li):

    t3 = templist.pop()
    t2 = templist.pop()
    t1 = templist.pop()
    telist = [t1, t2, t3]

    return calculation(telist)



def calculation(li):
    result = 0

    if li[2] == '+':
        result = int(li[0]) + int(li[1])
    elif li[2] == '/':
        result = int(li[0]) // int(li[1])
    elif li[2] == '*':
        result = int(li[0]) * int(li[1])
    elif li[2] == '-':
        result = int(li[0]) - int(li[1])
    return result









T = 10

for t in range(T):
    token = ['(', '+', '-', '*', '/', ')']
    l = int(input())
    S = list(input())
    # print(S)
    signlist = list()
    stacklist = list()
    count = 0
    for s in S:

        # print(s)
        if s in token:
            # print('index', token.index(s))
            # print('in',s)
            if s == token[0]:
                count += 1
                signlist.append(s)
            elif s == token[5]:
                # print(signlist)
                te = signlist.pop()
                while te != token[0]:
                    stacklist.append(te)
                    te = signlist.pop()
                    # print('te', te)
            elif token.index(s) > 2:
                if len(signlist) > 0:
                    while token.index(signlist[len(signlist)-1]) > 2:
                        k = signlist.pop()
                        stacklist.append(k)
                    signlist.append(s)
            else:
                if len(signlist) > 0 and token.index(signlist[len(signlist)-1]) > 2:
                    f = signlist.pop()
                    stacklist.append(f)
                signlist.append(s)
        else:
            stacklist.append(int(s))
        # print(signlist)
        # print(stacklist)
    while len(signlist) != 0:
        stacklist.append(signlist.pop())

    stacklist = stacklist[::-1]

    templist = list()
    total = 0
    while True:
        if len(stacklist) == 0:
            if len(templist) == 1:
                total = templist[0]
            break
        temp = stacklist.pop()

        if temp not in ['+', '/', '-', '*']:
            templist.append(int(temp))

        elif temp in ['+', '/', '-', '*']:
            templist.append(temp)
            tempa = totalcal(templist)
            stacklist.append(tempa)

    print(f"#{t+1} {total}")

