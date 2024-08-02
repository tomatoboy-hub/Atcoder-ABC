N,K = map(int,input().split())
A = list(map(int,input().split()))

ans = K*(K+1) // 2
s = set()
for i in range(N):
    if A[i] <= K:
        s.add(A[i]) 
    
t_sum = sum(s)
print(ans - t_sum)