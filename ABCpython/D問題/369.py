"""
dpやろなあ感
dp[i][j] = i番目のモンスターに会った時倒すのがj回目の時 える経験値の最大

dp[i][j] = dp[i-1][j-1 % 2] + A[i] , dp[i-1][j % 2]
dp[i][j-1] = dp[i-1][j % 2] + A[i], dp[i-1][j % 2]

"""
N = int(input())

A = [0] + list(map(int,input().split()))
dp = [[0] * 2 for _ in range(N+1)]

dp[1][1] =  max(A[1], dp[0][1])


for i in range(2,N+1):
    dp[i][0] = max(dp[i-1][1] + A[i] * 2, dp[i-1][0])
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] + A[i])

print(max(dp[N])) 


