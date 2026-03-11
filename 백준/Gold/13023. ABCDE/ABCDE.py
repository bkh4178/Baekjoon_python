import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, depth):
    if depth == 4: return 1
    visited[v] = 1
    
    for i in graph[v]:
        if visited[i] == 0:
            if dfs(i, depth+1) == 1: return 1

    visited[v]=0 #끝까지 갔지만, 주위에 아무도 없었다면 다시 전으로 돌아가서 다른 노드로 가야 하는데 그땐 방문 여부 초기화가 필요함
    return 0


for v in range(N):
    visited = [0]*N
    if dfs(v,0):
        print(1)
        exit()

print(0)