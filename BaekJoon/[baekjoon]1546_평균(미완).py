N = int(input())

inputlist = list(map(int, input().split()))
inputsum = sum(inputlist)
inputmax = max(inputlist)
print(round(inputsum/inputmax*100/N, 2))