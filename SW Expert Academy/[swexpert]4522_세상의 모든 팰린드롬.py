
def palicol(b):
    if len(b) == 0 or len(b) == 1:
        return True
    else:
        if b[0] == b[len(b)-1] or (b[0] == '?' or b[-1] == '?'):
            dc = ""
            for q in range(1, len(b)-1):
                dc += b[q]
            return palicol(dc)
        else:
            return False

T = int(input())

for t in range(T):
    s = input()
    if palicol(s):
        print(f'#{t+1} Exist')
    else:
        print(f'#{t+1} Not exist')