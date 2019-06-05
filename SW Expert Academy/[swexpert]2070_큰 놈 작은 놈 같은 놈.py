
str = ""
t = int(input())
a = ""
for i in range(t):
    li = list(map(int, input().split()))
    if li[0] > li[1]:
        a = ">"
    elif li[0] < li[1]:
        a = "<"
    else:
        a = "="
    str += f'#{i+1} {a}\n'
print(str)