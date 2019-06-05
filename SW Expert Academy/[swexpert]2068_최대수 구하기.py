

str = ""
t = int(input())
for i in range(t):
    li = list(map(int, input().split()))
    str += f'#{i+1} {max(li)}\n'
print(str)