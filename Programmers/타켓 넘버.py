from collections import deque
from copy import deepcopy
def solution(numbers, target):
    answer = 0
    targetlist = deque()
    number = numbers.pop(0)
    targetlist.append(number)
    targetlist.append(0-number)
    for number in numbers:
        templist = deque()
        while len(targetlist) > 0:
            target_num = targetlist.pop()
            templist.append(target_num+number)
            templist.append(target_num-number)
        targetlist = deepcopy(templist)
    for targli in targetlist:
        if targli == target:
            answer += 1
    
    return answer



print(solution([1, 1, 1, 1, 1], 3))