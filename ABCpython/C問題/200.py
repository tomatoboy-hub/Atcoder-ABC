N = int(input())
A = list(map(int,input().split()))

from collections import Counter

for i in range(N):
    A[i] = A[i] % 200

c = Counter(A)
ans = 0
for k,v in c.items():
    ans += v*(v-1) // 2 

print(ans)