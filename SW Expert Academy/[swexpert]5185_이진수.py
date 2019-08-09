def Bbit_return(i):
    output = ""
    for j in range(3, -1, -1):
        output += "1" if i & (1<<j) else "0"
    return output

T = int(input())

for t in range(T):

    N, nstring = input().split()

    N = int(N)

    result = ""

    for n in range(N):
        result += Bbit_return(int('0x{}'.format(nstring[n]), 16))

    print('#{} {}'.format(t+1, result))