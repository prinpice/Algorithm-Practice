
def finda(n):
    if len(n) == 1:
        return n
    
    sum = 0
    for i in range(len(n)-1, 0, -1):
        sum += n//(10**i)
        n = n% (10**i)
    return finda(n)


for t in range(int(input())):
    n = int(input())
    result = finda(n)
    print(f'#{t+1} {result}')