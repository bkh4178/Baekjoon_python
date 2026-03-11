import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r, c):
    visited[r][c] = 1
    dx = [+1, +1, +1, -1, -1, -1, 0, 0]
    dy = [0, +1, -1, 0, +1, -1, +1, -1]
    for d in range(8):
        nr = r + dx[d]
        nc = c + dy[d]
        if 0<=nr<h and 0<=nc<w and graph[nr][nc]==1 and visited[nr][nc]==0:
            dfs(nr, nc)

cnt_list = []

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    visited = [[0]*w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    cnt_list.append(cnt)

for cnt in cnt_list: print(cnt)