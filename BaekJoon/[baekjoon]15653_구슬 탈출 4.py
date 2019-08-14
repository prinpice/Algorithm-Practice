
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS():
    global N, M
    for d in range(4):



N, M = map(int, input().split())

maplist = [list(input()) for _ in range(N)]
redpoint, bluepoint, holepoint = (), (), ()
red_visited = [["-" for _ in range(M)] for _ in range(N)]
blue_visited = [["-" for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if maplist[i][j] == "R":
            redpoint = (i, j)
            red_visited[i][j] = "s"
        if maplist[i][j] == "B":
            bluepoint = (i, j)
            blue_visited[i][j] = "s"
        if maplist[i][j] == "O":
            holepoint = (i, j)

