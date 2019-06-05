
T = int(input())
for t in range(T):
    s = input()
    for i in ["a", "e", "i", "o", "u"]:
        if i in s:
            s = s.replace(i, "")
    print(f'#{t+1} {s}')

