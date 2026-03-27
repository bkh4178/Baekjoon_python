import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e10)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(i):
    q = deque([i])
    visited = [-1]*(N+1)
    visited[i] = 0
    
    while q:
        current = q.popleft()
        for new in graph[current]:
            if visited[new] == -1:
                visited[new] = visited[current] + 1
                q.append(new)
    
    return sum(visited[1:])

min_num = INF
ind = 0
for i in range(1,N+1):
    bacon = BFS(i)
    if bacon < min_num:
        min_num = bacon
        ind = i
print(ind)