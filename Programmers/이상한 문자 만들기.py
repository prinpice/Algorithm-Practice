def solution(s):
    answer = ""
    string_list = s.split(" ")
    for idx, val in enumerate(string_list):
        val_list = list(val)
        for idx_alpha, alpha in enumerate(val_list):
            if idx_alpha % 2 == 0:
                val_list[idx_alpha] = alpha.upper()
        string_list[idx] = "".join(val_list)
    answer = " ".join(string_list)
    return answer

print(solution("o o o"))