import sys
sys.stdin = open("1218.txt", "r")

def findpoint(idx, value):
    # print(idx, value)
    global result
    if idx == -1:
        result = 0
        return
    if visited[idx] == 0:
        if value == ")":
            if str[idx] == "(":
                visited[idx] = 1
            else:
                result = 0
        if value == "}":
            if str[idx] == "{":
                visited[idx] = 1
            else:
                result = 0
        if value == "]":
            if str[idx] == "[":
                visited[idx] = 1
            else:
                result = 0
        if value == ">":
            if str[idx] == "<":
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
        if value == ")" or value == "]" or value == "}" or value == ">":
            visited[idx] = 1
            # print(visited)
            findpoint(idx-1, value)

        if result == 0:
            break
    if 0 in visited:
        result = 0
        # print(*visited, sep=" | ")
    print(f"#{t+1} {result}")

