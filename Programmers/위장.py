from itertools import combinations
def solution(clothes):
    answer = 0
    cloths = {}
    for arr in clothes:
        if arr[1] not in cloths.keys():
            cloths[arr[1]] = [arr[0]]
        else:
            cloths[arr[1]].append(arr[0])
    print(cloths)
    print(list(combinations(cloths)))


    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))