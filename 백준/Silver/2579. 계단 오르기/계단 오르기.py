import sys
input = sys.stdin.readline

N = int(input())
stair = [0] + [int(input()) for _ in range(N)]

dp = [0]*(N+1) # dp[i] : ith계단을 반드시 밟았을 때 최고 점수
dp[1] = stair[1]
if N >=2 :
    dp[2] = stair[1]+stair[2]

for i in range(3, N+1):
    dp[i] = max(stair[i]+dp[i-2], stair[i]+stair[i-1]+dp[i-3])

print(dp[N])