N,M,K = map(int,input().split())

"""
dp[i][j] i番目まで決めて総和がjのものの数
"""
MOD = 998244353
dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(K):
        for k in range(1,M+1):
            if j + k > K:
                break
            dp[i+1][j + k] += dp[i][j]
            dp[i+1][j + k] % MOD
print(sum(dp[-1]) % MOD)