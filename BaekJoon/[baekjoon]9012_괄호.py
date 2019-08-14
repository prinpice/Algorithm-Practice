import sys
sys.stdin = open("괄호.txt", "r")

T = int(input())

for _ in range(T):
    str = input()
    templist = []
    result = "YES"
    for st in str:
        if st == "(":
            templist.append(st)
        elif st == ")":
            if len(templist):
                templist.pop()
            else:
                result = "NO"
    if len(templist):
        result = "NO"
    print(result)