from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1

    visited = deque()
    bridge_truck = []
    while True:
        if len(visited) > 0 and visited[0][0] + bridge_length == answer:
            visited.popleft()
            bridge_truck.pop(0)
        
        if len(truck_weights) > 0 and sum(bridge_truck) + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            visited.append((answer, truck))
            bridge_truck.append(truck)
    
        if len(visited) == 0:
            break
    
        answer += 1

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))