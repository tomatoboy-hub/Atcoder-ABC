N = int(input())
A = list(map(int,input().split()))
keta = [0] * (10 + 1)
MOD = 998244353
for a in A:
    keta[len(str(a))] += 1

su = sum(A)
ans = 0
for i in range(N-1):
    a = A[i]
    keta[len(str(a))] -=1
    su -= a

    ans += a*sum([10 ** i * keta[i] for i in range(len(keta))]  )
    ans += su

    ans %= MOD

print(ans)