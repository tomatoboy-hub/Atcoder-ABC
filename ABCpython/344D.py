T = input()
N = int(input())
S = []
for _ in range(N):
    AS = list(map(str,input().split()))
    S.append(AS[1:])

INF = 10 ** 10
dp = [[INF] * (len(T) + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(len(T) + 1):
        for s in S[i]:
            if j >= len(s) and s == T[j - len(s):j]:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - len(s)] + 1)
        dp[i + 1][j] = min(dp[i+1][j],dp[i][j])

result = dp[N][len(T)]
if result == INF:
    print(-1)
else:
    print(result)