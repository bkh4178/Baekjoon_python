def solution(n, info):
    answer = [-1]
    max_diff = 0
    
    def is_better(new, old):
        # 낮은 점수부터 비교해야 하므로 뒤에서부터 확인
        for i in range(10, -1, -1):
            if new[i] > old[i]:
                return True
            elif new[i] < old[i]:
                return False
        return False
    
    def dfs(idx, arrows, ryan):
        nonlocal answer, max_diff
        
        # 0점까지 다 본 경우
        if idx == 11:
            if arrows > n:
                return
            
            # 남은 화살은 0점에 몰아넣기
            ryan[10] += n - arrows
            
            apeach_score = 0
            ryan_score = 0
            
            for i in range(11):
                score = 10 - i
                
                if info[i] == 0 and ryan[i] == 0:
                    continue
                
                if ryan[i] > info[i]:
                    ryan_score += score
                else:
                    apeach_score += score
            
            diff = ryan_score - apeach_score
            
            if diff > 0:
                if diff > max_diff:
                    max_diff = diff
                    answer = ryan[:]
                elif diff == max_diff and is_better(ryan, answer):
                    answer = ryan[:]
            
            # 원상복구
            ryan[10] -= n - arrows
            return
        
        # 선택 1: 현재 점수를 이긴다
        need = info[idx] + 1
        if arrows + need <= n:
            ryan[idx] = need
            dfs(idx + 1, arrows + need, ryan)
            ryan[idx] = 0
        
        # 선택 2: 현재 점수를 포기한다
        dfs(idx + 1, arrows, ryan)
    
    dfs(0, 0, [0] * 11)
    
    return answer