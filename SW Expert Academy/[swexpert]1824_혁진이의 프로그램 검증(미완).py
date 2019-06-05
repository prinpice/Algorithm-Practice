def move(li, n1, n2, a):
    if '<':
        if n2 == 0:
            n2 = len(li[n1])-1
        else:
            n2 -= 1
    elif '>':
        if n2 == len(li[n1])-1:
            n2 = 0
        else:
            n2 += 1
    elif '^':
        if n1 == 0:
            n1 = len(li)-1
        else:
            n1 -= 1
    elif 'v':
        if n1 == len(li)-1:
            n1 = 0
        else:
            n1 += 1
    elif '_':
       #  if a == 0 
        pass
    te = [n1, n2]
    return te
        


T = int(input())
R, C = map(int, input().split())
for _ in range(R):
    li = input()