N, K = map(int,input().split())
R = list(map(int,input().split()))

import itertools

candidates = list(itertools.product(*[range(1,x + 1) for x in R]))

for c in candidates:
    if (sum(c) % K == 0):
        print(*c)