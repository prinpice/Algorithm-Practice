def solution(dartResult):
    answer = 0
    dart = list(dartResult)
    num = 0
    dartlist = list()
    while num < len(dart):
        le = len(dartlist)
        
        if dart[num] == '*':
            dartlist[le-1] *= 2
            if le-1 != 0:
                dartlist[le-2] *= 2
            
            
            # for idx in range(le):
                # dartlist[idx] *= 2
            # print(dartlist)
        elif dart[num] == '#':
            dartlist[le-1] *= -1
            # print(dartlist)

        else:
            da = 0
            if dart[num + 1] == '0':
                da = int((dart[num]+dart[num+1]))
                num += 1
            else:
                da = int(dart[num])
            # print(dart[num])
            dartlist.append(da)
            num += 1
            # print(dart[num])
            temp = dartlist[le]
            if dart[num] == 'D':
                dartlist[le] = temp**2
                # print("D", dartlist)
            elif dart[num] == 'T':
                
                dartlist[le] = temp**3
                # print("T", dartlist)
        num += 1
    answer = sum(dartlist)
    return answer


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))