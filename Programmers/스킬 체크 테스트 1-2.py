def solution(arr1, arr2):
    answer = []
    for idx1, val1 in enumerate(arr1):
        temp_answer = list()
        for idx2, val2 in enumerate(val1):
            temp_answer.append((val2+arr2[idx1][idx2]))
        answer.append(temp_answer)
    return answer

print(solution([[1], [2]], [[3], [4]]))