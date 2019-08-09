def preorder_traverse(T):
    global count
    if T:
        # print("%d" % T, end=' ')
        count += 1
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])

T = int(input())

for t in range(T):

    E, N = map(int, input().split())

    templist = list(map(int, input().split()))
    templi = list()
    for temp in templist:
        if temp not in templi:
            templi.append(temp)

    tree = [[0] * 2 for _ in range(len(templi)+1)]

    for i in range(len(templist) // 2):
        parent, child = templist[i * 2], templist[i * 2  + 1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
    count = 0
    preorder_traverse(N)
    # print()
    print('#{} {}'.format(t+1, count))