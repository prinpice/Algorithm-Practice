

N = int(input())


maxnum = N//5

for num in range(maxnum, -2, -1):
    
    if num == -1:
        print(num)
        break
    elif (N-num*5)%3 == 0:
        print(num + (N-num*5)//3)
        break
    