def solution(arrangement):
    answer = 0
    stacklist = list()
    minus = 0
    for arrange in arrangement:
        if arrange == '(':
            minus = 0
            stacklist.append(arrange)
        else:
            minus += 1
            stacklist.pop()
            if minus == 1:
                answer += len(stacklist)
            else:
                answer += 1

    return answer



print(solution("()(((()())(())()))(())"))