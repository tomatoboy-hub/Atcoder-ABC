N,X = map(int,input().split())
J = [(0,0)]
for _ in range(N):
    a,b = map(int,input().split())
    J.append((a,b))

"""
dp[i][j] i番目までのジャンプでjに入れるかどうか
"""

dp = [[False] * (X+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(1, N+1):
    for j in range(X + 1):
        if j - J[i][0] >= 0:
            dp[i][j] |= dp[i-1][j - J[i][0]]
        if j - J[i][1] >= 0:
            dp[i][j] |= dp[i-1][j - J[i][1]]

print("Yes" if dp[N][X] else "No")