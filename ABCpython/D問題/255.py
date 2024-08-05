from itertools import accumulate
import bisect
N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
acc_A = list(accumulate(A))
for _ in range(Q):
    X = int(input())
    ans = 0
    if X < A[0]:
        ans = acc_A[N] - X* N
    elif A[N-1] <= X:
        ans = X * N - acc_A[N]
    else:
        ind = bisect.bisect_right(A,X)
        ans += X*(ind) -  acc_A[ind-1] 
        ans += (acc_A[-1] - acc_A[ind-1]) - X * (N - ind)
    print(abs(ans))