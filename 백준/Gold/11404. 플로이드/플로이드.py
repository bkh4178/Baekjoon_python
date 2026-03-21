import sys
input = sys.stdin.readline
INF = int(1e10)

n, m = int(input()), int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    if w < graph[a][b]:
        graph[a][b] = w

for k in range(1,n+1):
    for i in range(1, n+1):
        if graph[i][k] != INF:
            for j in range(1, n+1):
                cost = graph[i][k]+graph[k][j]
                if cost < graph[i][j]:
                    graph[i][j] = cost

for i in range(1, n+1):
    print(*(0 if graph[i][j]==INF else graph[i][j] for j in range(1, n+1)))