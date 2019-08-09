

def even(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

TC = int(input())

for tc in range(TC):
    num = int(input())
    print(f'#{tc+1} {even(num)}')

