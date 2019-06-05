
str = ""
t = int(input())
for i in range(t):
    li = list(map(int, input().split()))
    a = round(sum(li)/len(li))
    str += f'#{i + 1} {a}\n'
print(str)