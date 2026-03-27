import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

N = int(input())
def dijkstra(start, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF]*(n+1)
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

for _ in range(N):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    distance = dijkstra(c, graph)
    count = 0
    max_num = 0
    for i in range(1, n+1):
        if distance[i] != INF: 
            count +=1
            if distance[i] > max_num: 
                max_num = distance[i]
    print(*[count, max_num])