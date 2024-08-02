from collections import Counter
from itertools import accumulate
N ,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(accumulate(A))
C = Counter()
C[0] += 1

ans = 0
for x in B:
    y = x - K
    ans += C[y]
    C[x] += 1

print(ans)