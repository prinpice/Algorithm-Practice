import sys
sys.stdin = open("5207.txt", "r")

def binarySearch(arr, low, high, key):
    if low > high:
        return 0
    else:
        middle = (low+high)//2
        if key == arr[middle]:
            return 1
        elif key < arr[middle]:
            return binarySearch(arr, low, middle-1, key)
        else:
            return binarySearch(arr, middle+1, high, key)

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    res = 0
    nlist.sort()
    print(nlist)
    for m in mlist:
        res += binarySearch(nlist, 0, N-1, m)
    print(f"#{t} {res}")