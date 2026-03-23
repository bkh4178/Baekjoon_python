import sys
input = sys.stdin.readline
import heapq
INF = int(1e10)
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
s, e = map(int, input().split())
dijkstra(s)

print(distance[e])