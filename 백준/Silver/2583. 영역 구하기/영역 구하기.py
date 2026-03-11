import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 1

def dfs(x, y):
    visited[y][x] = 1
    cnt = 1
    dx = [+1, -1, 0, 0]
    dy = [0, 0, +1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and graph[ny][nx] == 0 and visited[ny][nx] == 0:
            cnt += dfs(nx, ny)
    return cnt

cnt_list = []
for x in range(N):
    for y in range(M):
        if visited[y][x] == 0 and graph[y][x]==0:
            cnt_list.append(dfs(x, y))
print(len(cnt_list))
cnt_list.sort()
for cnt in cnt_list: print(cnt, end = ' ')