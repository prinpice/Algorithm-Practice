def solution(n, computers):
    answer = 0
    
    computer_list = [[] for _ in range(len(computers))]
    visited = [1 for _ in range(n)]

    for idx, computer in enumerate(computers):
        for idx2, com in enumerate(computer):
            if idx != idx2 and com == 1:
                computer_list[idx].append(idx2)
    # print(computer_list)
    # print(visited)

    for num in range(n):
        if visited[num] == 1:
            visited[num] = 0
            stacklist = [num]
            while len(stacklist) > 0:
                val = stacklist.pop(0)
                if len(computer_list[val]) > 0:
                    for value in computer_list[val]:
                        if visited[value] == 1:
                            visited[value] = 0
                            stacklist.append(value)
            answer += 1




    return answer



print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))