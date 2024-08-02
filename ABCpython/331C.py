from collections import Counter,defaultdict

N = int(input())
A = list(map(int,input().split()))

C = Counter(A)
D = []
all_sum = sum(A)

for key in C:
    D.append([key,key*C[key]])

D_sorted = sorted(D, key=lambda item: item[0])


for i in range(1,len(D)):
    D_sorted[i][1] += D_sorted[i-1][1]
al = defaultdict(int)
for d in D_sorted:
    al[d[0]] = d[1]

ans = []
for a in A:
    ans.append(all_sum - al[a])

print(*ans)   