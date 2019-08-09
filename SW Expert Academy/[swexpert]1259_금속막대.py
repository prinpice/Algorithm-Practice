"""
원형 금속 막대를 가장 길게 연결하고자 한다. 원형 금속 막대는 한 쪽 면에 수나사와 다른 쪽에 암나사로 이루어져 있다.

수나사와 암나사는 굵기가 서로 다르다. 아래 그림에서 수나사의 굵기는 3을 암나사의 굵기는 4를 나타내고 있다.

이후 나사의 굵기를 수나사의 굵기 x 암나사의 굵기로 표현한다. 연결은 +로 표현한다.
 

 

이와 같은 원형 금속 막대를 연결하기 위해서는 수나사의 굵기와 암나사의 굵기가 서로 일치해야 한다.

예를 들어 두 개의 원형 금속 막대 3x4와 4x5가 있을 때 3x4+4x5로 연결해야 연결되며 4x5+3x4로 연결하면 연결되지 않는다.
 


수나사와 암나사의 크기가 서로 다른 여러 개의 원형 금속 막대를 가장 많이 연결하려고 한다.

어떤 순서로 연결해야 가장 많이 연결하는지를 찾는 프로그램을 작성하시오.

[입력]

맨 첫 줄에는 테스트 케이스의 개수가 주어진다.

그리고 테스트 케이스가 각 라인에 주어진다. 각 테스트 케이스는 2줄로 구성되며, 첫 줄에는 원형 금속 막대의 개수 n이 주어지고, 다음 줄에는 2n개의 수가 주어진다. 

숫자는 공백으로 구분한다. 앞에서부터 2개씩 하나의 원형 금속 막대의 수나사 굵기와 암나사 굵기를 의미한다.
 
[출력]

각 테스트 케이스 각각에 대한 답을 출력한다.

각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음, 각 테스트 케이스에 주어진 수열로부터 가장 많이 연결하기 위한 원형 금속 막대의 수나사 굵기와 암나사 굵기를 순서대로 출력한다.
"""
"""
10
3
3 4 2 3 4 5
4
1 2 5 1 2 4 4 3
"""
"""
#1 2 3 3 4 4 5
#2 5 1 1 2 2 4 4 3
"""

TC = int(input())

for c in range(TC):

    n = int(input())
    an = list(map(int, input().split()))

    counti = 0
    while True:
        idx = 0
        counta = 0
        for a in an:
            if an.count(a) % 2 != 0:
                idx = an.index(a)
                if idx % 2 == 0:
                    an[0], an[idx] = an[idx], an[0]
                    an[1], an[idx+1] = an[idx+1], an[1]
                else:
                    an[len(an)-2], an[idx-1] = an[idx-1], an[len(an)-2]
                    an[len(an)-1], an[idx] = an[idx], an[len(an)-1]
                counti += 1
                break
            counta+= 1
        if counti != 0:
            if an.count(an[0]) % 2 != 0 and an.count(an[len(an)-1]) != 0:
                break
        elif counta == len(an):
            break

        print(f'an {an}')
        
    for i in range(1, len(an)-2, 2):
        if an[i] != an[i+1]:
            for j in range(i+1, len(an)-1, 2):
                if an[j] == an[i]:
                    an[i+1], an[j] = an[j], an[i+1]
                    an[i+2], an[j+1] = an[j+1], an[i+2]
        print(f'an2 {an}')

    print(f'#{c+1}', " ".join(list(map(str, an))))

