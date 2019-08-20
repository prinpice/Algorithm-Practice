import sys
sys.stdin = open('10952.txt', 'r')

for _ in range(int(input())):
    inputlist = list(map(int, input().split()))
    N = inputlist.pop(0)
    avgnum = sum(inputlist)/N
    count = 0
    for num in range(len(inputlist)):
        if inputlist[num] > avgnum:
            count+= 1
    print("{}%".format(round(count/N*100, 3)))
