N, K = map(int,input().split())
A = list(map(int,input().split()))

ans = 10 << 60
A.sort()
for i in range(0,K+1):
    ans = min(ans ,A[i+N-K-1]-A[i])

print(ans)