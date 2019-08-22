def convert(n):
    T = "0123456789ABCDEF"
    q, r = divmod(n, 3)
    if q == 0:
        return T[r]
    else:
        return convert(q) + T[r]

def solution(n):
    answer = ''
    temp_answer = str(convert(n))
    for ans in temp_answer:
        if ans == '0':
            answer +='4'
        elif ans == '1':
            answer += '1'
        else:
            answer += '2'
    if n % 3 == 0:
        answer = answer[1:]
    return answer

print(solution(int(input())))