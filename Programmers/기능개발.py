import math
def solution(progresses, speeds):
    answer = []
    count = 0
    day = 0
    for num in range(len(progresses)):
        this_day = math.ceil((100-progresses[num])/speeds[num])
        if day < this_day:
            if day != 0:
                answer.append(count)
            day = this_day
            count = 1
        else:
            count += 1
    answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))