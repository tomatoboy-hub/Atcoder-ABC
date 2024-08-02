N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
INF = 1 << 60
ans = [INF] * N

for i in range(2 * N):
    ans[(i+1) % N] = min(ans[i % N] + S[i % N], T[(i + 1) % N])

for x in ans:
    print(x)