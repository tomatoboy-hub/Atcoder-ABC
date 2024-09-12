N,K = map(int,input().split())
S = []
for _ in range(N):
    s = input()
    S.append(s)

"""
bit全探索で
"""

ans = 0

for bitnum in range(1 << N):
    ans_tmp = 0
    Choosed = []
    for shift in range(N):
        if bitnum >> shift & 1:
            Choosed.append(S[shift])
    for code in range(97,123):
        Alphabet = chr(code)
        InCount = 0
        for T in Choosed:
            if Alphabet in T:
                InCount += 1

        if InCount == K:
            ans_tmp += 1
    ans = max(ans_tmp,ans)

print(ans)