import sys
input = sys.stdin.readline

N = int(input()) #사람의 수
long = list(map(int, input().split())) #본인보다 키 큰 사람 왼쪽에 몇명인지

result = [] # 빈 리스트 
for i in range(N-1, -1, -1):
    result.insert(long[i], i+1)

print(*result)