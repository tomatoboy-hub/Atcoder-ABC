N = int(input())

"""
dp[i][j] = i桁目にjとする時の組み合わせ
"""

dp = [[0] * 9 for _ in range(N)]
for j in range(9):
    dp[0][j] = 1
MOD = 998244353
for i in range(1,N):
    dp[i][0] += dp[i-1][1]%MOD + dp[i-1][0] % MOD
    dp[i][8] += dp[i-1][7]%MOD + dp[i-1][8] % MOD
    for j in range(1,8):
        dp[i][j] +=(dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % MOD

print(sum(dp[N-1])%MOD)
