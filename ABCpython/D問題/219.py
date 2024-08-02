N = int(input())
X,Y = map(int,input().split())
INF = 1000
dp = [[[INF] * (Y + 1) for _ in range(X+1)] for _ in range(N+1)]

mat = []
for _ in range(N):
    a,b = map(int,input().split())
    mat.append((a,b))

dp[0][0][0] = 0
for i in range(N):
    x,y = mat[i]
    for j in range(X + 1):
        jj = min(j + x, X)
        for k in range(Y + 1):
            dp[i+1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            kk = min(k+y,Y)
            dp[i+1][jj][kk] = min(dp[i + 1][jj][kk], dp[i][j][k]+1)

print(dp[N][X][Y] if dp[N][X][Y] < INF else -1)
