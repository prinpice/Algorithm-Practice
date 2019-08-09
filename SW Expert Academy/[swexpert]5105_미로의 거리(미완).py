def isSafe(maze, x, y):
    global N
    if x >= 0 and x < N and y >= 0 and y < N and maxe[x][y]:
        return True
    return False

def solveMaze(maxe):
    global N
    sol = [[0 for j in range(n)] for i in range(N)]

    if solveMazeUtil(maxe, 0, 0, sol) == False:
        print("Solution doexn't exist")
        return False
    print(maxe)
    print(sol)
    return True

def solveMaxeUtil(maxe, x, y, sol):
    global N
    if x == N-1 and y == N-1:
        sol[x][y] = 1
        return True

    if isSafe(maxe, x, y) == True:
        sol[x][y] = 1

        if solveMaxeUtil(maze, x+1, y, sol) == True:
            return True

        if solveMaxeUtil(maze, x, y+!, sol) == True:
            return True

        sol[x][y] = 0
        return False

T = int(input())

for t in range(T):
    N = int(input())
    mirolist = [0] * N
    for n in range(N):
        mirolist[n] = list(map(int, (",".join(input())).split(',')))

    print(mirolist)
    solveMaxe(maze)