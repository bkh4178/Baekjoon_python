def solution(info, edges):
    answer = 0
    
    graph = [[] for _ in range(len(info))]
    
    for parent, child in edges:
        graph[parent].append(child)
    
    def dfs(sheep, wolf, candidates):
        nonlocal answer
        
        answer = max(answer, sheep)
        
        for node in candidates:
            next_sheep = sheep
            next_wolf = wolf
            
            if info[node] == 0:
                next_sheep += 1
            else:
                next_wolf += 1
            
            # 늑대가 양 이상이면 이 경로는 실패
            if next_wolf >= next_sheep:
                continue
            
            # 현재 node는 방문했으므로 후보에서 제거
            # 대신 node의 자식들을 후보에 추가
            next_candidates = candidates[:]
            next_candidates.remove(node)
            next_candidates.extend(graph[node])
            
            dfs(next_sheep, next_wolf, next_candidates)
    
    # 0번 루트는 항상 양
    dfs(1, 0, graph[0])
    
    return answer