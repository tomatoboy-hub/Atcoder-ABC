N = int(input())
T = list(map(int,input().split()))
t_sum = sum(T)
dp = [[False] * (t_sum + 1) for _ in range(N)]

""" dp[i][j] = i番目までの料理を作る時にj時間となれるかどうか"""

dp[0][T[0]] = True
for i in range(1,N):
    dp[i][T[i]] = True 
    for j in range(t_sum + 1):
        
        if j - T[i] >= 0:
            dp[i][j] = dp[i-1][j] | dp[i-1][j - T[i]]        
        dp[i][j] = dp[i][j] | dp[i-1][j]

t_sum = sum(T)
ans = 10 << 20
for j in range(t_sum + 1):
    if dp[N-1][j] == True:
        ans = min(ans , max(j, t_sum - j))

print(ans)