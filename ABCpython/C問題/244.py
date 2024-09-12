N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
"""
dp[i][j] i番目にjを使った時に満たしているかどうか?
"""

dp = [[False] * 2 for _ in range(N)]
dp[0][0] = True
dp[0][1] = True

for i in range(1,N):
    if abs(A[i] - A[i-1]) <= K and dp[i-1][0]:
        dp[i][0] = True
    if abs(A[i] - B[i-1]) <= K and dp[i-1][1]:
        dp[i][0] = True
    if abs(B[i] - A[i-1]) <= K and dp[i-1][0]:
        dp[i][1] = True
    if abs(B[i] - B[i-1]) <= K and dp[i-1][1]:
        dp[i][1] = True
print("Yes" if dp[N-1][0] or dp[N-1][1] else "No")
