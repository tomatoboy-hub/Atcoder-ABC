T = input()
N = int(input())
AS = []
for _ in range(N):
    AS.append(list(input().split()))

"""
dp[i][j] = i番目までの袋を見た時にTのj番目までの文字列を作るのに必要な最小コスト
"""
INF = 10 ** 10
dp = [[INF] * (len(T) + 1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(len(T) + 1):
        for s in AS[i][1:]:
            if j >= len(s) and T[j - len(s):j] == s:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j-len(s)] + 1)
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])

result = dp[N][len(T)]
if result == INF:
    print(-1)
else:
    print(result)
