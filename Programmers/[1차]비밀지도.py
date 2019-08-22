def solution(n, arr1, arr2):
    answer = []
    for ar1 in arr1:
        print(len(bin(ar1)[2:]))
    return answer



print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))