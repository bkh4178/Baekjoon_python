import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

def is_valid(x,y):
    check = 0<=x<len(graph[0]) and 0<=y<len(graph) and graph[y][x]==1 and visited[y][x] == False
    return check

def BFS(x, y):
    global graph, visited
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True
    num = 1 # 현재 집 포함
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if is_valid(nx, ny):
                visited[ny][nx] = True
                queue.append((nx, ny))
                num += 1
    
    return num

result = []
for x in range(N):
    for y in range(N):
        if graph[y][x] == 1 and visited[y][x] == False:
            result.append(BFS(x,y))

result.sort()

print(len(result))
for n in result:
    print(n)