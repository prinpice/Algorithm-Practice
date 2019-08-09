T = int(input())

for t in range(T):
    N = int(input())
    nlist = [input() for _ in range(N)]
    # 'A': 65
    sublist = [[] for _ in range(65)]
    for na in nlist:
        sublist[ord(na[0])].append(na)
    print(nlist)
