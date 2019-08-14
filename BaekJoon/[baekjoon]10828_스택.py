import sys
sys.stdin = open("스택.txt", "r")


N = int(input())
stacklist = []
for _ in range(N):
    templist = list(input().split())
    # print(templist)
    if templist[0] == 'push':
        stacklist.append(int(templist[1]))
    elif templist[0] == 'pop':
        if len(stacklist):
            print(stacklist.pop())
        else:
            print(-1)
    elif templist[0] == 'size':
        print(len(stacklist))
    elif templist[0] == "empty":
        if len(stacklist):
            print(0)
        else:
            print(1)
    elif templist[0] == "top":
        if len(stacklist):
            print(stacklist[-1])
        else:
            print(-1)
