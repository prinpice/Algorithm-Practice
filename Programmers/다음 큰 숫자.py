def solution(n):
    answer = 0
    p = bin(n)
    p = p[2:]
    print(p)
    print(type(p))
    for num in range(len(p)-1, -1, -1):
        if p[num] == 1 and p[num-1] == 0:
            p = p[:num-1] + "10" + p[num+1:]
            print(p)
            break
    print(p)
    answer = int(p, 2)

    return answer

print(solution(78))
print(solution(15))