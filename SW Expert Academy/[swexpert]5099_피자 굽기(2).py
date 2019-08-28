import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

for t in range(int(input())):
    N, M = map(int, input().split())
    queue_list = deque()
    pizza_list = list(map(int, input().split()))
    for idx, val in enumerate(pizza_list):
        queue_list.appendleft((idx+1, val))
        
