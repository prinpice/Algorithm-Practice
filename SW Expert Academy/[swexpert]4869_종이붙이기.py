# nCr
# 팩토리얼(분자)
def factorial(n):
    if n < 2:
        return 1
    return n*factorial(n-1)

# n부터 -1씩 뺀 값을 r개 곱하기(분모)
def factor(n, r):
    res = 1
    for i in range(r):
        res *= n-i
    return res

# nCr
def combination(n, r):
    if r > n/2:
        r = n-r
    re = int(factor(n, r)/factorial(r))
    return re

T = int(input())

for t in range(T):
    result = 0
    N = int(input())
    n = N//10
    for k in range(n//2+1):
        result += (combination(n-k, k))*(2**k)

    print('#{} {}'.format(t+1, result))