import sys
input = sys.stdin.readline
INF = int(1e10)
V, E = map(int, input().split())
graph = [[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

min_cy = INF
for k in range(1, V+1):
    for i in range(1, V+1):
        if graph[i][k] != INF:
            for j in range(1, V+1):
                if graph[k][j] != INF:
                    cost = graph[i][k]+graph[k][j]
                    if cost < graph[i][j]:
                        graph[i][j] = cost

min_cy = min([graph[i][i] for i in range(1, V+1)])
print(-1 if min_cy == INF else min_cy)