N = int(input())
S = input()
C = list(map(int,input().split()))
INF = 1 << 50
dp = [[[INF] * (2) for _ in range(2)]for _ in range(N)]
"""
dp[i][v][f]
Si文字目まで見た時に Si が vの時 同じ文字の箇所がfこの時にの最小コスト
"""
if S[0] == "0":
    dp[0][0][0] = 0
    dp[0][1][0] = C[0]
else:
    dp[0][1][0] = 0
    dp[0][0][0] = C[0]

for i in range(1, N):
    if S[i] == "0":
        dp[i][0][0] = dp[i-1][1][0]
        dp[i][0][1] = min(dp[i-1][0][0],dp[i-1][1][1])
        dp[i][1][0] = dp[i-1][0][0] + C[i]
        dp[i][1][1] = min(dp[i-1][0][1], dp[i-1][1][0]) + C[i]

    else: 
        dp[i][1][0] = dp[i-1][0][0]
        dp[i][1][1] = min(dp[i-1][0][1], dp[i-1][1][0])
        dp[i][0][0] = dp[i-1][1][0] + C[i]
        dp[i][0][1] = min(dp[i-1][0][0],dp[i-1][1][1]) + C[i]

ans = min(dp[N -1][0][1], dp[N-1][1][1])
print(ans)