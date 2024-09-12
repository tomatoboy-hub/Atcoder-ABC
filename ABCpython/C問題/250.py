N,Q = map(int ,input().split())
from collections import defaultdict
val2idx = defaultdict(int)
idx2val = defaultdict(int)
for i in range(1,N+1):
    val2idx[i] = i
    idx2val[i] = i


for i in range(Q):
    x = int(input())
    idx = val2idx[x]
    if idx != N:
        change_val = idx2val[idx + 1]
        idx2val[idx+1] = x
        val2idx[change_val] = idx 
        val2idx[x] = idx + 1
        idx2val[idx] = change_val
    else:
        change_val = idx2val[idx - 1]
        idx2val[idx-1] = x
        val2idx[change_val] = idx 
        val2idx[x] = idx - 1
        idx2val[idx] = change_val

for i in range(1,N+1):
    print(idx2val[i])
