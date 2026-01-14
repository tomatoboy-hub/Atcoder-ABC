T = int(input())
MAX = 10 ** 9

for _ in range(T):
    N = int(input())
    S = input()
    ans = 0
    dp = [[MAX] * 3 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        if S[i-1] == "1":
            dp[i][0] = dp[i-1][0] + 1
            dp[i][1] = min(dp[i-1][0],dp[i-1][1])
            dp[i][2] = min(dp[i-1][1] , dp[i-1][2]) + 1
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = min(dp[i-1][0],dp[i-1][1]) + 1
            dp[i][2] = min(dp[i-1][1],dp[i-1][2])
    ans = min(dp[N])
    print(ans)