t = int(input())
# N : 학생수 , K: 학점을 알고싶은 학생의 번호
N, K = map(int, input().split())
str = ""
for i in range(t):
    scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    li = []
    # k번째 학생총점
    k_sc = 0
    for j in range(n):
        # 학생이 받은 m : 중간시험점수, f : 기말시험점수, h : 과제점수
        m, f, h = map(int, input().split())
        li.append(m*0.35 + f*0.45 + h*0.2)
        if j == k:
            k_sc = m*0.35 + f*0.45 + h*0.2
    li.sort()
    li.reverse()
    score = ""
    for l in range(len(li)):
        if li[l] == k_sc:
            score = scores[l]
            break
    print(f'#{t+1} {score}')