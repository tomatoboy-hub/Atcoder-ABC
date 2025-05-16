from collections import Counter
N,D = map(int,input().split())
A = list(map(int,input().split()))
M = 10 ** 6 + 1
def solve(lst):
    """
    dp[i][j] = i番目まで決めて末尾がjであるときの最大値
    """
    n = len(lst)
    dp = [[0] * 2 for _ in range(n+1)]
    for i in range(n):
        dp[i+1][0] = max(dp[i][1],dp[i][0])
        dp[i+1][1] = dp[i][0] + lst[i]
    mx = max(dp[n][0],dp[n][1])
    sum_lst = sum(lst)
    return sum_lst - mx

cnt = [0] * M
for x in A:
    cnt[x] += 1

if D == 0:
    print(sum(max(x-1,0) for x in cnt))
    exit()

ans = 0
for i in range(D):
    ans += solve(cnt[i::D])
print(ans)