def solution(n, words):
    answer = []
    turn = 1
    person = 1
    visited = []
    for idx, word in enumerate(words):
        if word in visited:
            return [person, turn]
        if idx == len(words)-1:
            # return [0, 0]
            answer = [0, 0]
            break
        if word[-1] != words[idx+1][0]:
            if person == n:
                return [1, turn + 1]
            else:
                return [person+1, turn]
        visited.append(word)
        person += 1
        if person > n:
            person = 1
            turn += 1

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, 	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))