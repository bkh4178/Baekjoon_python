import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
# 인접행렬 만들기 (adj. matrix)
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1 # edge로 연결된 부분 =1, 나머진 0

visited = [0]*(N+1)

def dfs(v):
    visited[v] = 1
    for i in range(1, N+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

count = 0

for v in range(1, N+1):
    if visited[v] == 0:
        dfs(v)
        count += 1

print(count)