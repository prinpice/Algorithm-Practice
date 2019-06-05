t = int(input())
str = ""
for i in range(t):
    li = list(map(int, input().split()))
    str += f'#{i+1} {li[0]//li[1]} {li[0]%li[1]}\n'
print(str)