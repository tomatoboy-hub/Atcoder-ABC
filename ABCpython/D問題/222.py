MOD = 998244353

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

CONST = 3001

dp = [[0] * CONST for _ in range(N + 1)]

dp[0][0] = 1

for i in range(N):
    a = A[i]
    b = B[i]
    s = sum(dp[i][:a]) % MOD
    for c in range(a,b + 1):
        s += dp[i][c]
        s %= MOD
        dp[i+1][c] = s

print(sum(dp[N]) % MOD)