import sys
input = sys.stdin.readline
INF = int(1e10)

n, m = int(input()), int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = min(w, graph[a][b]) # 노선이 하나가 아닐 수도 있기 때문

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph[1:]:
    for j in range(1, n+1):
        if row[j] == INF: row[j] = 0
    print(*row[1:])