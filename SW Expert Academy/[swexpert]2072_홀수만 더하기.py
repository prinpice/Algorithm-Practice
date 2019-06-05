
t =  int(input())
str = ""
for i in range(t):
    li = list(map(int, input().split()))
    a = 0
    for j in li:
        if j % 2 != 0:
            a += j
    str += f'#{i+1} {a}\n'
print(str)