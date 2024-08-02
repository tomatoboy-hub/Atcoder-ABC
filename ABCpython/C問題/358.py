N,M = map(int,input().split())
""" bit全探索かなんかで 2 ** 10 の1024通りかな"""

S = []
for _ in range(N):
    s = input()
    S.append(s)

ans = M + 10

for bit in range(1 << N):
    store = []
    for i in range(N):
        if bit >> i & 1:
            store.append(i)

    data = [0] * M
    for s_i in store:
        for j,s_j in enumerate(S[s_i]):
            if s_j == "o":
                data[j] = 1

    if data == [1] * M:
        ans = min(ans,len(store))

print(ans)
 