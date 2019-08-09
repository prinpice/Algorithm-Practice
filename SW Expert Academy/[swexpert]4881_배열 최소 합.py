T = int(input())

for t in range(T):
    N = int(input())
    arraylist = [0]*N
    for n in range(N):
        arraylist[n] = list(map(int, input().split()))
    print(min(arraylist))



    print(f'#{t+1} ')