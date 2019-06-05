T = int(input())

for t in range(T):
    inputlist = list(map(int, input().split()))
    total = 0
    if inputlist[4] <= inputlist[2]:
        if inputlist[0] * inputlist[4] < inputlist[1]:
            total = inputlist[0] * inputlist[4]
        else:
            total = inputlist[1]
    else:
        if inputlist[0] * inputlist[4] < inputlist[1] + (inputlist[4]-inputlist[2]) * inputlist[3]:
            total = inputlist[0] * inputlist[4]
        else:
            total = inputlist[1] + (inputlist[4]-inputlist[2]) * inputlist[3]
    print(f'#{t+1} {total}')