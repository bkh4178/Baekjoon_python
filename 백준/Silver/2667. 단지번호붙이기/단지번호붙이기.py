import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

def is_valid(row,col):
    check = 0<=col<len(graph[0]) and 0<=row<len(graph) and graph[row][col]==1
    return check

def BFS(row, col):
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    queue = deque()
    graph[row][col] = 2
    queue.append((row,col))
    num = 1 # 현재 집 포함
    while queue:
        cur_row, cur_col = queue.popleft()
        for i in range(4):
            nrow = cur_row + dx[i]
            ncol = cur_col + dy[i]

            if is_valid(nrow, ncol):
                graph[nrow][ncol] = 2
                queue.append((nrow, ncol))
                num += 1
    
    return num

result = []
for row in range(N):
    for col in range(N):
        if graph[row][col] == 1:
            result.append(BFS(row,col))

result.sort()

print(len(result))
for n in result:
    print(n)