N,M=map(int,input().split())
X = [0] +list(map(int,input().split()))
B=[0]*(N+1)

for i in range(M):
    c,y = map(int,input().split())
    B[c] = y

dp = [[0] * (N+1) for _ in range(N+1)]
"""
i番目のコイントスでカウンタの値が j の時の最大額
"""

for i in range(1, N+1):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = max(dp[i-1])
        else:
            dp[i][j] = dp[i-1][j-1] + X[i] + B[j]

print(max(dp[N]))




