N,S,M,L=map(int,input().split())
"""
dp[i] = i個の卵を買う時の最小コスト
"""
INF = 10 ** 10
dp=[INF] * (N + 13)

dp[0] = 0
for i in range(1,N + 12):
    if i >= 6:
        dp[i] = min(dp[i],dp[i - 6] + S)
    if i >= 8:
        dp[i] = min(dp[i],dp[i-8] + M)
    if i >= 12:
        dp[i] = min(dp[i],dp[i-12] + L)

print(min(dp[N:]))
