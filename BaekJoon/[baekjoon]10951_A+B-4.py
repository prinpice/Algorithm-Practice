import sys
sys.stdin = open('10952.txt', 'r')

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
    