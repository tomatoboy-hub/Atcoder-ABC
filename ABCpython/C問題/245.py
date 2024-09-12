N,K,X = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
i = 0
while K > 0 and i < len(A):
    if A[i] / X <= K:
        A[i] %= X
        K -= A[i] // X
    else:
        A[i] -= K * X
        K = 0
    i += 1 

print(A)
print(sum(A))