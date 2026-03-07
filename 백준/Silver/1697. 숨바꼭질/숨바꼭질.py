import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
dist = [-1 for _ in range(100000+1)]

def BFS(x):
    dist[x] = 0
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()
        if x == K: return dist[x]
        for nx in (x-1, x+1, x*2):
            if 0<=nx<len(dist) and dist[nx]==-1:
                dist[nx] = dist[x]+1
                queue.append(nx)
        
print(BFS(N))