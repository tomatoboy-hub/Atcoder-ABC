N = int(input())
A = list(map(int,input().split()))
MOD = 998244353
dp = [[0] * 10 for _ in range(N)]

dp[0][A[0] % 10] = 1

for i in range(1, N):
    for j in range(10):
        A[i] %= 10
        dp[i][(j * A[i]) % 10] += dp[i-1][j] % MOD
        dp[i][(j + A[i]) % 10] += dp[i-1][j] % MOD
for j in range(10):
    print(dp[N-1][j] % MOD)


 