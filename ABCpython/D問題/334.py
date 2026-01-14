N,Q = map(int,input().split())
R = list(map(int,input().split()))
from itertools import accumulate
R.sort()
acc_R = list(accumulate(R))
for _ in range(Q):
    x = int(input())
    ans = 0
    l = 0
    r = N 
    while  l < r:
        mid = (l + r) // 2
        if acc_R[mid] > x:
            r = mid 
        else:
            l = mid + 1
    ans = l
    print(ans)