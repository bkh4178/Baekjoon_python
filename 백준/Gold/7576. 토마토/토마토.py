import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def BFS():
    dx=[-1,+1,0,0]
    dy=[0,0,+1,-1]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1: queue.append((i,j))

    while queue:
        cur_row, cur_col= queue.popleft()
        for i in range(4):
            nrow = cur_row + dx[i]
            ncol = cur_col + dy[i]

            if 0<=ncol<len(graph[0]) and 0<=nrow<len(graph) and graph[nrow][ncol]==0: 
                queue.append((nrow,ncol))
                graph[nrow][ncol] = graph[cur_row][cur_col] + 1

    if 0 in [graph[i][j] for i in range(N) for j in range(M)]:
        return -1
                
    return max(max(row) for row in graph) - 1

print(BFS())