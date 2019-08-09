TC = int(input())

for tc in range(TC):
    str1 = input()
    str2 = input()

    result = 0

    for s in range(len(str2) - len(str1) + 1):
        if str2[s] == str1[0]:
            i = 0
            for i in range(len(str1)):
                if str1[i] != str2[s + i]:
                    i = len(str1)+1
                    break
            if i != len(str1)+1:
                result = 1
                break


    print(f'#{tc+1} {result}')