import sys
sys.stdin = open("1218.txt", "r")

open_values = ['(', '{', '[', '<']
close_values = [')', '}', ']', '>']

def findpoint(idx, value):
    # print(idx, value)
    global result
    if idx == -1:
        result = 0
        return
    if visited[idx] == 0:
        for findidx in range(4):
            if value == close_values[findidx]:
                if str[idx] == open_values[findidx]:
                    visited[idx] = 1
                else:
                    result = 0
        return
    elif visited[idx] == 1:
        findpoint(idx-1, value)



for t in range(10):
    N = int(input())
    str = input()

    visited = [0 for _ in range(N)]
    for idx, value in enumerate(str):
        result = 1
        if value in close_values:
            visited[idx] = 1
            # print(visited)
            findpoint(idx-1, value)

        if result == 0:
            break
    if 0 in visited:
        result = 0
        # print(*visited, sep=" | ")
    print(f"#{t+1} {result}")

