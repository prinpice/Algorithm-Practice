def solution(s, n):
    answer = ''
    str_list = list(s)
    for idx, alphabet in enumerate(str_list):
        
        if alphabet != ' ':
            val = ord(alphabet)
            if 65 <= val <= 90:
                val += n
                if val > 90:
                    val -= 26
            if 97 <= val <= 122:
                val += n
                if val > 122:
                    val -= 26
            str_list[idx] = chr(val)
    answer = "".join(str_list)

    return answer


print(solution("a B z", 4))