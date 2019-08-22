def solution(answers):
    answer = []
    temp_answer = [0, 0, 0]
    temp1 = [1, 2, 3, 4, 5]
    temp2 = [2, 1, 2, 3, 2, 4, 2, 5]
    temp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1 = 0
    count2 = 0
    count3 = 0
    for idx, val in enumerate(answers):
        if temp1[count1] == val:
            temp_answer[0] += 1
        if temp2[count2] == val:
            temp_answer[1] += 1
        if temp3[count3] == val:
            temp_answer[2] += 1
        count1 += 1
        count2 += 1
        count3 += 1
        if count1 == 5:
            count1 = 0
        if count2 == 8:
            count2 = 0
        if count3 == 10:
            count3 = 0
    ma = max(temp_answer)
    for num in range(3):
        if temp_answer[num] == ma:
            answer.append(num+1)

    return answer

print(solution([1, 2, 3, 4, 5]))