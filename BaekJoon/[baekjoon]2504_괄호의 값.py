import sys
sys.stdin = open("괄호의 값.txt", "r")


str = input()

result = ""
stacklist = []

for st in str:
    if st == "(" or st == "[":
        if len(stacklist):
            if stacklist[-1] == ")" or stacklist[-1] == "]":
                result += "+"
            stacklist.pop()
            if len(stacklist):
                stacklist.pop()
            else:
                result = 0
                break
        stacklist.append(st)
    elif st == ")":
        if len(stacklist):
            if stacklist[-1] == "(":
                result += "2"
            elif stacklist[-1] == "[":
                result += "3"
            elif stacklist[-1] == ")" or stacklist[-1] == "]":
                result += "*"
            stacklist.append(st)
if len(stacklist):
    result = 0
else:
    result = list(result)
print(result)
