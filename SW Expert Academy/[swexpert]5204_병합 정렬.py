import sys
sys.stdin = open("5204.txt", "r")

def merge(left, right):
    result = []
    if left[-1] > right[-1]:
        global cnt
        cnt += 1

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    # print("next", result)
    return result


def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

T = int(input())

for t in range(1, T+1):

    N = int(input())
    cnt = 0
    nlist = list(map(int, input().split()))
    relist = merge_sort(nlist)
    print(f"#{t} {relist[N//2]} {cnt}")



