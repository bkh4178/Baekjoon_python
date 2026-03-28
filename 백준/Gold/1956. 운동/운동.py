import sys
input = sys.stdin.readline

INF = int(1e10)

def floyd(graph, V):
    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

def main():
    V, E = map(int, input().split())

    graph = [[INF] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    floyd(graph, V)

    answer = INF
    for i in range(1, V + 1):
        answer = min(answer, graph[i][i])

    print(-1 if answer == INF else answer)

if __name__ == "__main__":
    main()