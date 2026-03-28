import sys
input = sys.stdin.readline

INF = 10**15

def floyd(dist, V):
    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

def main():
    V, E = map(int, input().split())

    dist = [[INF] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        dist[a][b] = c

    floyd(dist, V)

    answer = INF
    for i in range(1, V + 1):
        answer = min(answer, dist[i][i])

    print(-1 if answer == INF else answer)

if __name__ == "__main__":
    main()