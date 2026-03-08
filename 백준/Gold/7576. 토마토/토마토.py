import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def is_valid(row,col):
    check = 0<=col<len(graph[0]) and 0<=row<len(graph) and graph[row][col]==0
    return check

def BFS():
    dx=[-1,+1,0,0]
    dy=[0,0,+1,-1]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1: queue.append((i,j,0))

    day_max = 0
    while queue:
        row, col, day = queue.popleft()
        if day > day_max : day_max = day
        for i in range(4):
            nrow = row + dx[i]
            ncol = col + dy[i]

            if is_valid(nrow,ncol): 
                queue.append((nrow,ncol,day+1))
                graph[nrow][ncol] = 1

    if 0 in [graph[i][j] for i in range(N) for j in range(M)]:
        return -1
                
    return day_max

print(BFS())