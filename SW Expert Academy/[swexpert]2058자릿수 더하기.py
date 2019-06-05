
a = int(input())
s = 0
for i in range(4):
    s += a//(10**(3-i))
    a = a%(10**(3-i))
print(s)