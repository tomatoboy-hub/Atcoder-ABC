N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
i = 0
j = 0
INF = 1000000000
ans = INF
while (i < N and j < M):
    ans = min(abs(A[i]-B[j]),ans)
    if A[i] < B[j]:
        i += 1
    else:
        j += 1
 
print(ans)

