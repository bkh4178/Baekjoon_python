#%%
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph1 = [list(input().strip()) for _ in range(N)]

visited1 = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]

def dfs(r, c, ver):
    # ver = 1 : 적록색약 아닌 사람, ver = 2 : 적록색약인 사람
    dx = [+1, -1, 0, 0]
    dy = [0, 0, +1, -1]
    if ver == 1:
        visited1[r][c] = 1
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0<=nr<N and 0<=nc<N and visited1[nr][nc]==0 and graph1[nr][nc] == graph1[r][c]:
                dfs(nr, nc, 1)
    else:
        visited2[r][c] = 1
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0<=nr<N and 0<=nc<N and visited2[nr][nc]==0:
                if graph1[nr][nc] in ['R', 'G'] and graph1[r][c] in ['R', 'G']:
                    dfs(nr, nc, 2)
                elif graph1[nr][nc] == 'B' and graph1[r][c] == 'B':
                    dfs(nr, nc, 2)

cnt1, cnt2 = 0, 0
for r in range(N):
    for c in range(N):
        if visited1[r][c] == 0:
            dfs(r,c,1)
            cnt1 += 1
        if visited2[r][c] == 0:
            dfs(r,c,2)
            cnt2 += 1
print(cnt1, cnt2)