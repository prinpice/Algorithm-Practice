def solution(n):
    answer = 0
    ans_list = list()
    num = 1
    while True:
        if num in ans_list or num > n:
            break
        if n % num == 0:
            ans_list.append(n//num)
            if num != n // num:
                ans_list.append(num)
        num += 1
    answer = sum(ans_list)
    return answer


print(solution(1))