def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck = list()
    truck_time = list()
    truck_now = truck_weights.pop(0)
    truck_time.append([answer, truck_now, answer + bridge_length])
    truck.append(truck_now)
    answer += 1
    while True:
        # print(truck, truck_time)
        if len(truck_weights) == 0 and len(truck) == 0:
            break
        else:
            if len(truck_time) != 0 and truck_time[0][2] == answer:
                truck_time.pop(0)
                truck.pop(0)
            if len(truck_weights) != 0:
                # print("sum", sum(truck) + truck_weights[0])
                while sum(truck) + truck_weights[0] <= weight:
                    
                    truck_now = truck_weights.pop(0)
                    truck_time.append([answer, truck_now, answer + bridge_length])
                    truck.append(truck_now)
                    answer += 1
                    # print("truck", truck, truck_time)
                    if len(truck_weights) == 0:
                        break
            print(truck_time, "now")
            if len(truck_time) != 0:
                answer = truck_time[0][2]
            # print(answer)
                


    return answer

print(solution(100, 100, [10]))