TC = int(input())

A = [i for i in range(1, 13)]
a = len(A)

for c in range(TC):
    n, k = map(int, input().split())
    count = 0
    
    for i in range(1<<a):
        suma = 0
        counta = 0
        for j in range(a+1):
            if i & (1<<j):
                suma += A[j]
                counta += 1
        if suma == k and counta == n:
            count += 1
    print(f'#{c+1}', count)