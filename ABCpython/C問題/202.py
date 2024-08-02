N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split())) 
B_C = []
for j in range(N):
    C[j] -= 1
    B_C.append(B[C[j]])

from collections import Counter
bc = Counter(B_C)
ac = Counter(A)

ans = 0
for k,v in bc.items():
    ans += v * ac[k]

print(ans)