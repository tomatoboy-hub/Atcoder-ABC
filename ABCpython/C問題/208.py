N, K = map(int,input().split())
A = list(map(int,input().split()))
indices = [*range(len(A))]
sorted_indices = sorted(indices, key=lambda i: A[i])

ans = [K // N] * N
K %= N
for i in range(K):
    ans[sorted_indices[i]] += 1
    
for a in ans:
    print(a)