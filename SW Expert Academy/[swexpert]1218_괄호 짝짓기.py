import sys
sys.stdin = open("1218.txt", "r")

def recursive(str):
    # print("str", str)
    # print(stacklist)
    global result
    if len(stacklist) == 0 and str == "":
        return
    if len(stacklist) != 0 and str == "":
        result = 0
        return
    now = str[0]
    str = str[1:]
    if now == "{" or now == "[" or now == "(" or now == "<":
        stacklist.append(now)
    else:
        if len(stacklist) == 0:
            result = 0
            return
        find = stacklist.pop()
        if now == "]":
            if find != "[":
                result = 0
                return
        elif now == "}":
            if find != "{":
                result = 0
                return
        elif now == ")":
            if find != "(":
                result = 0
                return
        elif now == ">":
            if find != "<":
                result = 0
                return
    recursive(str)


for t in range(13):
    N = int(input())
    str = input()
    stacklist = []
    result = 1
    recursive(str)
    print(f"#{t+1} {result}")
