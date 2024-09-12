N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append(s)
from collections import defaultdict

dic = defaultdict(set)
for i in range(N):
    for j in range(10):
        k = j
        while k in dic[S[i][j]]:
            k += 10
        dic[S[i][j]].add(k)
tmp_max = 0
ans = 10 ** 10
for item in dic.values():
    tmp_max = max(item)
    ans = min(ans,tmp_max)

print(ans)