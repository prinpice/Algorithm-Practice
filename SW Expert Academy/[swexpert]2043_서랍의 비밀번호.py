# "123 100"
# ["123", "100"]

# input().split()
# a = int(input().split()[0])
# b = int(input().split()[1])

# list(map(int, input().split()))
# [123, 100]
# a, b = list(map(int, input().split()))
# a, b = [123, 100]
# (a, b) = (123, 100)
# a, b = map(int, input().split())
# a. b = [int(x) for x in input().split()]

P, K = map(int, input().split())
print(P - K + 1)