X, A, D,N = map(int,input().split())
l = [i for i in range(A,A + D * N,D)]

import bisect

lind = bisect.bisect_left(l,X)

print(min(abs(l[lind-1] - X),abs(l[lind] - X)))