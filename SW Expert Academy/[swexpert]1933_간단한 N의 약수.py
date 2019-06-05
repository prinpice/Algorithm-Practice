a = int(input())
li = []
for i in range(1, a+1):
    if a%i == 0:
        li.append(str(i))
print(" ".join(li))
