T = int(input())

for t in range(T):
    N = float(input())

    count = 1
    use = 0.5
    result = ""
    while count < 13 and N > 0:
        if 0 <= N-use :
            N -= use
            result += "1"
        else:
            result += "0"

        use *= (1/2)
        count += 1

    if count == 13 and N != 0:
        result = "overflow"
    print("#{} {}".format(t+1, result))