def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    answer = 0

    def dfs(fatigue, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(n):
            need, cost = dungeons[i]

            if not visited[i] and fatigue >= need:
                visited[i] = True
                dfs(fatigue - cost, count + 1)
                visited[i] = False

    dfs(k, 0)
    return answer