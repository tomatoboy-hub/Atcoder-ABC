N,M = map(int,input().split())
A = [0] + list(map(int,input().split()))
dp = [[ 10 ** -15] *( N + 1) for _ in range(M + 1)]
for x in range(1, N+ 1):
    dp[1][x] = A[x]

for k in range(2, M+1):
    dpMax = dp[k-1][0]
    for x in range(k, N + 1):
        dpMax = max(dp[k-1][x-1],dpMax)
        dp[k][x] = dpMax + k * A[x]

print(max(dp[M]))