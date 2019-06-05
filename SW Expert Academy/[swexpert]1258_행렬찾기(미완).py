import sys
sys.stdin = open("1258.txt", "r")

def ffind(testli, startpoint, r):
    num = 0
    nowpoint = startpoint[:]
    # print("now", nowpoint[0])
    while testli[nowpoint[0]][nowpoint[1]] != 0:
        # print("nowpoint", nowpoint)
        num += 1
        nowpoint[r] += 1
    # print("exit")
    return num


T = int(input())

for t in range(T):
    N = int(input())

    # if N <= 10:
    #     submatrixnum = 5
    # elif N <= 40:
    #     submatrixnum = 10
    # elif N <= 80:
    #     submatrixnum = 15
    # else:
    #     submatrixnum = 20

    testli = [list(map(int, input().split())) for _ in range(N)]
    # print(testli)
    result = []
    resultmul = []
    temp0 = 0
    temp1 = 0
    for i in range(N):
        for j in range(N):
            if testli[i][j] != 0:
                startpoint = [i, j]
                temp0 = ffind(testli, startpoint, 1)
                # print("temp1", temp0, temp1)
                # print(startpoint)
                temp1 = ffind(testli, startpoint, 0)

                # print("temp2", temp0, temp1)
                if result == []:
                    result.append([temp0, temp1])
                    resultmul.append(temp0 * temp1)
                    # print("Result1", result, resultmul)
                else:
                    # print("else")
                    for re in resultmul:
                        # print(re, temp0*temp1)
                        if re > temp0 * temp1:
                            te = resultmul.index(re)
                            # print("te", te)
                            result.insert(te, [temp0, temp1])
                            resultmul.insert(te, temp0 * temp1)
                            break
                        elif temp0*temp1 > max(resultmul):
                            result.append([temp0, temp1])
                            resultmul.append(temp0*temp1)
                        elif temp0*temp1 == re:
                            te = resultmul.index(re)
                            if temp1 < result[te][1]:
                                result.insert(te, [temp0, temp1])
                                resultmul.insert(te, temp0 * temp1)
                                break
                            elif temp1 > result[te][1]:
                                if result[te] == max(resultmul):
                                    result.append([temp0, temp1])
                                    resultmul.append(temp0*temp1)
                                else:
                                    result.insert(te+1, [temp0, temp1])
                                    resultmul.insert(te+1, temp0 * temp1)
                                    break





                    # print("result2", result)

                for p in range(startpoint[0], startpoint[0] + temp1):
                    for q in range(startpoint[1], startpoint[1] + temp0):
                        testli[p][q] = 0
                # print(testli)
    # print("Result", result)
    print(f"#{t+1} {len(result)}", end=" ")
    for k in range(len(result)):
        for l in range(len(result[k])-1, -1, -1):
            print(result[k][l], end=" ")
    print()









