import sys
sys.stdin = open('10952.txt', 'r')



inputlist = []
for _ in range(9):
    inputlist.append(int(input()))
maxnum = max(inputlist)
print(maxnum)
for outnum in range(len(inputlist)):
    if inputlist[outnum] == maxnum:
        print(outnum+1)
        break
