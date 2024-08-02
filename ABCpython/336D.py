N = int(input())
A = list(map(int,input().split()))
INF = 0
dp_u = [INF] * N
dp_d = [INF] * N

dp_u[0] = 1
dp_d[-1] = 1

for i in range(N-1):
    dp_u[i+1] = min(dp_u[i]+1,A[i+1])

for i in range(N-1,0,-1):
    dp_d[i-1] = min(dp_d[i]+1, A[i-1])

result = 1
for i in range(N):
    result = max(result,min(dp_u[i],dp_d[i]))

print(result)