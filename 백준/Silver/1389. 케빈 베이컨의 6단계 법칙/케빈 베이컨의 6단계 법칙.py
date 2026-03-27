#%%
import sys
input = sys.stdin.readline
INF = int(1e10)

N, M = map(int, input().split())
graph = [[INF]* (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        if graph[i][k] != INF:
            for j in range(1, N+1):
                if graph[j][k] != INF:
                    cost = graph[i][k] + graph[k][j]
                    if graph[i][j] > cost:
                        graph[i][j] = cost

min_num = INF
ind = 0
for i in range(1, N+1):
    s = sum(graph[i][1:])
    if s < min_num:
        min_num, ind = s, i

print(ind)