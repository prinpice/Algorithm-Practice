import sys
sys.stdin = open('10952.txt', 'r')

inputlist = set([int(input())%42 for _ in range(10)])
print(len(inputlist))

