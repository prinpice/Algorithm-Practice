TC = int(input())
for i in range(TC):
    s, n = map(int, input().split())
    s_li = list(map(int, s))
    s_t_li = reversed(sorted(s_li))
    if s_l