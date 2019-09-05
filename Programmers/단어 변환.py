from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    visited = [0 for _ in range(len(words))]

    if target not in words:
        return 0
    queue.appendleft((0, begin))
    while len(queue) > 0:
        word_idx, word = queue.pop()
        if word == target:
            return word_idx
        for idx, val in enumerate(words):
            if visited[idx] == 0:
                count = 0
                
                for i, v in enumerate(val):
                    if word[i] != v:
                        count += 1
                    if count > 1:
                        break
                else:
                    queue.appendleft((word_idx+1, val))
                    visited[idx] = 1


    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))