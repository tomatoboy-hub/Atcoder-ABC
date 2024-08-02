S = "?" + input()
t = "?chokudai"
"dp[i][j] = sのi文字目まで使った時にtのi文字目となる通り"
MOD = 10 ** 9 + 7
dp = [ [0] * (len(t) + 1)  for _ in range(len(S) + 1)]
for i in range(len(S)):
    dp[i][0] = 1
for i in range(1,len(S)):
    for j in range(1,len(t)):
        if S[i] == t[j]:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j]
print(dp[len(S)-1][len(t)-1] % MOD)