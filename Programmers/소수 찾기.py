def solution(n):
    answer = 0
    result_list = [0 for _ in range(n)]
    result_list[0] = 1
    for num in range(1, n):
        mul = 2
        exnum = 0
        while exnum < n:
            exnum = (num+1) * mul
            if exnum-1 < n:
                result_list[exnum-1] = 1
                mul += 1
            else:
                break
    answer = result_list.count(0)
        

    return answer

print(solution(5))