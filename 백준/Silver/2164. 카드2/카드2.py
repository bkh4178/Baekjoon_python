from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque(range(1, n+1))

while len(q) > 1:
    q.popleft()          # 맨 위 카드 버림
    q.append(q.popleft())  # 그 다음 카드 맨 뒤로

print(q[0])