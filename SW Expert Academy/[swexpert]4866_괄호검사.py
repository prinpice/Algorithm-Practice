T = int(input())

for t in range(T):
    S = input()
    li = [0,0,0]
    for s in S:
        if s =='(':
            li[0] += 1
        elif s == '{':
            li[1] += 1
        elif s == '[':
            li[2] += 1
        elif s == ')':
            li[0] -= 1
        elif s == '}':
            li[1] -= 1
        elif s == ']':
            li[2] -= 1
    result = 1
    for i in li:
        if i != 0:
            result = 0
    print('#{} {}'.format(t+1, result))