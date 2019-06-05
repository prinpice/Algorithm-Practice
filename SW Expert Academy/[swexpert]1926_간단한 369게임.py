
N = int(input())
li = [str(i) for i in range(1, N+1)]
for j in range(len(li)):
    num = 0
    num += li[j].count("3")
    num += li[j].count("6")
    num += li[j].count("9")
    if num == 1:
      li[j] = "-"
    elif num == 2:
      li[j] = "--"

print(" ".join(li))
