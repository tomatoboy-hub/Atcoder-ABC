from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

def prime_factors(N):
    v = N
    p = defaultdict(int)
    for i in range(2, N):
        if i * i > N:
            break
        while v % i == 0:
            p[i] += 1
            v //= i
    if v != 1:
        p[v] += 1
    print(p)
    return p


# 素因数分解して奇数個の素数だけ残してグループにする各グループの NC2 の和が答え
# 0 だけ特別扱いする

B = defaultdict(int)
for a in A:
    factors_ = prime_factors(a)
    # 各因数を 2 で割る
    factors = {}
    for k, v in factors_.items():
        if v % 2 == 1:
            factors[k] = 1
    # Python は dict はキーにできないので tuple に変換する
    B[tuple(sorted(factors.items()))] += 1
    
ans = 0
for k, v in B.items():
    if k == ((0, 1),):
        # 0 は他のすべての値とペアになる
        ans += v * (v - 1) // 2 + v * (N - v)
    else:
        # それ以外はそのまま NC2
        ans += v * (v - 1) // 2

print(ans)