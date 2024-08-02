N = int(input())
A = list(map(int,input().split()))

pos = [-1] * (N+1)

for i,a in enumerate(A):
    pos[a] = i

ans = []
for i in range(N):
    if A[i] != i + 1:
        targ = pos[i + 1]
        A[i],A[targ] = A[targ], A[i]
        pos[A[targ]] = targ
        ans.append((i + 1, targ + 1) )
print(len(ans))
for a,b in ans:
    print(a,b)


    