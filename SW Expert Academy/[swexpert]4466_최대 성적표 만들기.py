

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    n_list = list(map(int, input().split()))
    sum = 0
    for k in range(K):
        sum+=n_list.pop(n_list.index(max(n_list)))
    print(f'#{t+1} {sum}')
    