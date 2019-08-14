import sys
sys.stdin = open('10952.txt', 'r')

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(a + b)