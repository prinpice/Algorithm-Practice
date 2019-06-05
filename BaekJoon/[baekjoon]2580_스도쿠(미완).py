import sys
sys.stdin = open("2580스도쿠.txt", "r")

def checkcheck(idx_y, idx_x):
    # 가로
    res = []
    for i in range(1, 10):
        if i not in sudokulist[idx_y]:
           res.append(i)
    # print(res)

    # 세로
    for re in res:
        for i in range(9):
            if sudokulist[i][idx_x] == re:
                res.remove(re)

    # 네모
    if idx_y < 3:
        temp_y = 0
    elif idx_y < 6:
        temp_y = 3
    else:
        temp_y = 6
    if idx_x < 3:
        temp_x = 0
    elif idx_x < 6:
        temp_x = 3
    else:
        temp_x = 6
    for re in res:
        for i in range(temp_y, temp_y+3):
            for j in range(temp_x, temp_x+3):
                # print(i, j)
                if sudokulist[i][j] == re:
                    res.remove(re)
    # print(idx_y,res)
    return res

def check(findlist):
    if len(findlist) == 0:
        for sudo in sudokulist:
            print(*sudo, sep=" ")
        # print(*sudokulist, sep="\n")
        # result = sudokulist.deepcopy() # Todo
        # print("================")
        return
    now_y, now_x = findlist.pop(0)
    # print(now_y, now_x)
    res = checkcheck(now_y, now_x)
    # print(res)
    for re in res:
        sudokulist[now_y][now_x] = re
        check(findlist)
        sudokulist[now_y][now_x] = 0

sudokulist = [[] for _ in range(9)]
findlist = []
for i in range(9):
    sudokulist[i] = list(map(int, input().split()))
    for findnum, value in enumerate(sudokulist[i]):
        if value == 0:
            findlist.append((i, findnum))
# print(*sudokulist, sep="\n")
# print(*findlist)
# print("=======start==========")

check(findlist)
## print(*res) # TODO
# print(*sudokulist, sep="\n")





# print(*sudokulist, sep="\n")
# print("==========start=========")
# visited = [[0 for _ in range(9)] for _ in range(9)]
# lastlist = []
# def checkcheck(idx_y, idx_x):
#     # 가로
#     res = []
#     for i in range(1, 10):
#         if i not in sudokulist[idx_y]:
#            res.append(i)
#     print(res)
#
#     # 세로
#     for re in res:
#         for i in range(9):
#             if sudokulist[i][idx_x] == re:
#                 res.remove(re)
#
#     # 네모
#     if idx_y < 3:
#         temp_y = 0
#     elif idx_y < 6:
#         temp_y = 3
#     else:
#         temp_y = 6
#     if idx_x < 3:
#         temp_x = 0
#     elif idx_x < 6:
#         temp_x = 3
#     else:
#         temp_x = 6
#     for re in res:
#         for i in range(temp_y, temp_y+3):
#             for j in range(temp_x, temp_x+3):
#                 # print(i, j)
#                 if sudokulist[i][j] == re:
#                     res.remove(re)
#     print(idx_y,res)
#     return res
#
# def check(idx_y):
#     global lastlist
#     print("idx", idx_y)
#     print(*sudokulist, sep="\n")
#     print("----------------")
#     if idx_y == 9 and len(lastlist) == 0:
#         lastlist = sudokulist[:]
#         print(len(lastlist))
#         return
#     print(*lastlist)
#     if not len(lastlist):
#         print("idxto", idx_y)
#         for findnum in range(9):
#             if sudokulist[idx_y][findnum] == 0:
#                 print(idx_y, findnum)
#                 res = checkcheck(idx_y, findnum)
#                 print("res", res)
#                 if not len(res):
#                     return
#                 for re in res:
#                     sudokulist[idx_y][findnum] = re
#                     print(*sudokulist, sep="\n")
#                     print("-=-=====-=-=-=-===--")
#                     check(idx_y)
#                     sudokulist[idx_y][findnum] = 0
#         check(idx_y+1)
#
#
# # for num in range(10):
# #     check(num)
# check(0)
#
# print(*lastlist)