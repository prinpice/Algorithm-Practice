
str = ""
t = int(input())
for i in range(t):
    s = input()
    y = s[0:4]
    m = int(s[4:6])
    d = int(s[6:])
    if m >= 1 and m <=12:
        if m == 2 and (d > 0 and d < 29):
            str += f'#{i+1} {s[0:4]}/{s[4:6]}/{s[6:]}\n'
        elif m in [4, 6, 9, 11] and (d > 0 and d < 31):
            str += f'#{i+1} {s[0:4]}/{s[4:6]}/{s[6:]}\n'
        elif m in [1, 3, 5, 7, 8, 10, 12] and (d>0 and d<32):
            str += f'#{i+1} {s[0:4]}/{s[4:6]}/{s[6:]}\n'
        else:
            str += f'#{i+1} -1\n'
    else:
        str += f'#{i+1} -1\n'
print(str)