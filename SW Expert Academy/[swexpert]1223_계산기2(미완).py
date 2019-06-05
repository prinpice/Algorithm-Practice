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

def totalcal(li):

    t3 = templist.pop()
    t2 = templist.pop()
    t1 = templist.pop()
    telist = [t1, t2, t3]

    return calculation(telist)


T = 10

for t in range(T):
    token = ['+', '-', '*', '/']
    N = int(input())
    nslist = list(input())
    templist = list()
    for nsnum in range(len(nslist)):
        if nslist[nsnum] not in token:
            templist 



    print(f"#{t+1} {total}")

