N,K,D = map(int,input().split())
A = [0] + list(map(int,input().split()))
"""
dp[i][j][k] = i番目目までの数字で j個選んだときに あまりがkとなる最大のもの
"""

dp = [[[-1] * D for i in range(K+1)] for j in range(N+1)]

for i in ranges(1, N+1):
    dp[i][1][A[i] % D] = A[i]

for i in range(2, N+1):
    for x in range(1, min(i+1,K+1)):
        for d in range(D):
            dp[i][x][d] = max(dp[i][x][d], dp[i-1][x][d])
            if dp[i-1][x-1][d] != -1:
                dp[i][x][(d + A[i]) % D] = max(dp[i][x][(d + A[i]) % D],dp[i-1][x-1][d]+A[i])

print(dp[N][K][0])