## 한 바퀴를 돌면 모든 피자의 치즈양이 C//2가 된다.
def solveCheese():
    global cheeselist, pizzalist
    for slicenum in range(len(cheeselist)):
        cheeselist[slicenum][1] = cheeselist[slicenum][1] // 2
    appendPizza()


## 치즈 양이 0인 곳에 대기중인 피자를 앞번호부터 순서대로 넣는다.
def appendPizza():
    global cheeselist, order, pizzalist, N
    # print("defcheeselist", cheeselist, "deforder", order, "defpizzalist", pizzalist)
    for rear in range(len(cheeselist)):
        if len(order) == M:
            # print("orderlen", order)
            return False
        if cheeselist[rear][1] == 0:
            if cheeselist[rear][0] not in order and cheeselist[rear][0] != 0:
                order.append(cheeselist[rear][0])
            if pizzalist != []:
                cheeselist[rear] = pizzalist.pop()
    # print("def1pizzalist", pizzalist, "def1cheeselist", cheeselist)
    solveCheese()


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    templist = list(map(int, input().split()))
    pizzalist = list()
    for tempnum in range(len(templist)):
        pizzalist.append([tempnum + 1, templist[tempnum]])
    # print("pizzalist", pizzalist)
    pizzalist.reverse()
    # print("reversepizza", pizzalist)
    cheeselist = [[0, 0] for _ in range(N)]
    order = list()
    appendPizza()
    # print(order[-1])
    print(f'#{t+1} {order[-1]}')