
"""
Kを素因数分解した時の素因数が全て出てくる時
Kの素数判定は可能 10 ** 6

"""

def prime_factorize(N):
    res = []
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            e += 1
            N //= p
        res.append((p,e))
    if N != 1:
        res.append((N,1))
    return res

K = int(input())
X = prime_factorize(K)
ans = 0

for x, num in X:
    rem = num
    for Nx in range(x, x*(num + 1), x):
        j = Nx
        while j % x == 0:
            j //= x
            rem -= 1
            if rem <= 0:
                break
        if rem <= 0:
            break
    ans  = max(Nx,ans)

print(ans)