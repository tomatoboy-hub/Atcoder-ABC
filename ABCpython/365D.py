N = int(input())
S = input()
"""
dpくさくて
dp[i][j] = i番目までで高橋くんがjの手を出した時に勝つ最大の数
"""

dp = [[0] * 3 for _ in range(N +1)]
for i in range(N):
    for j in range(3):
        if S[i] == "R":
            dp[i+1][1] = max(dp[i][0] + 1, dp[i][2] + 1)
            dp[i+1][0] = max(dp[i][1], dp[i][2])
        elif S[i] == "P":
            dp[i+1][2] = max(dp[i][0] + 1, dp[i][1] + 1)
            dp[i+1][1] = max(dp[i][0], dp[i][2])
        else:
            dp[i+1][0] = max(dp[i][1] + 1, dp[i][2] + 1)
            dp[i+1][2] = max(dp[i][0], dp[i][1])
    
print(max(dp[N]))