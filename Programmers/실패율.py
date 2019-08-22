def solution(N, stages):
    answer = []
    stagearray = [[0 for _ in range(len(stages))] for _ in range(N)]
    for stagenum in range(len(stages)):
        for num in range(stages[stagenum]-1):
            stagearray[num][stagenum] = 1
        if stages[stagenum]-1 < N:
            stagearray[stages[stagenum]-1][stagenum] = 2

    per = []
    for fail in stagearray:
        cou = fail.count(1)+fail.count(2)
        if cou == 0:
            per.append(0)
        else:
            per.append((fail.count(2)/cou))
    
    while per.count(-1) != N:
        ma = max(per)
        for idx in range(len(per)):
            if per[idx] == ma:
                answer.append(idx+1)
                per[idx] = -1
    return answer
print(solution(5, [2, 1, 2, 4, 2, 4, 3, 3]))