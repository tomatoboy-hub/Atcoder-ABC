from itertools import accumulate
import bisect
N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
acc_A = list(accumulate(A))
left = 0
right = max(A)
while (right - left) > 1:
    mid = (right + left) // 2
    ind = bisect.bisect_right(A,mid)
    spend = acc_A[ind-1]
    spend += mid * (N - ind)
    if spend > M:
        right = mid
    else:
        left = mid
print("infinite" if left >= max(A) else left)