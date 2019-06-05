
def confirm(li):
    for k in range(9):
        count = 0
        for j in range(9):
            if li[k] == li[j]:
                count += 1
        if count == 2:
            return 0
    return 1


T = int(input())

for t in range(T):
    li = [0] * 9
    for i in range(9):
        li[i] = list(map(int, input().split()))


    result = 1
    # 행 확인
    for m in range(9):
        if confirm(li[m]) == 0:
            result = 0

            break

    if result == 1:
        # 열 확인
        col_li = [0] * 9
        for n in range(9):
            h = 0
            for l in range(9):
                col_li[h] = li[l][n]
                h += 1

            if confirm(col_li) == 0:

                result = 0
                break

    if result == 1:
        # 네모 확인

        b = 0
        c = 0
        while True:
            rec_li = [0] * 9
            a = 0
            for p in range(3):
                for q in range(3):
                    rec_li[a] = li[b + p][c + q]
                    a += 1

            if confirm(rec_li) == 0:

                result = 0
                break

            if c + 3 < 9:
                c += 3

            elif c + 3 == 9:
                c = 0
                b += 3
            if b == 9:
                break
    print(f'#{t+1} {result}')