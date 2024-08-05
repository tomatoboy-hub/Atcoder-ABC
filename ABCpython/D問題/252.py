from collections import Counter

def comb(n,r):
    num = 1
    den = 1
    for i in range(r):
        num *= (n-i)
        den *= (r-i)
    return num // den

N = int(input())
A = list(map(int,input().split()))
C = Counter(A)

ans = comb(N,3)
for c in C.values():
    ans -= comb(c,2) * (N - c)
    ans -= comb(c,3)

print(ans)
