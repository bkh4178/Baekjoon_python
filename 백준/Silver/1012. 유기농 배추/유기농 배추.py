import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    visitied[y][x] = 1
    dx = [+1, -1, 0, 0]
    dy = [0, 0, +1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N and visitied[ny][nx]==0 and graph[ny][nx]==1:
            dfs(nx, ny)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    visitied = [[0]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    cnt = 0
    for x in range(M):
        for y in range(N):
            if graph[y][x]==1 and visitied[y][x]==0:
                dfs(x, y)
                cnt += 1
    print(cnt)