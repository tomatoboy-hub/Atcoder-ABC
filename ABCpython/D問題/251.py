import numpy as np
N,A,B = map(int,input().split())
max_sum = (N+1)*N//2
qa = N //A
qb = N //B
C = np.lcm(A,B)
qc = N // (C)

sa = A*(qa+1)*qa//2
sb = B*(qb+1)*qb//2
sc = C*(qc+1)*qc//2
ans = max_sum - sa -sb + sc

print(ans)


