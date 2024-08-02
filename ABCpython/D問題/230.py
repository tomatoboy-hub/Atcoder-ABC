N,D = map(int,input().split())
LR = []
for _ in range(N):
    l,r = map(int,input().split())
    LR.append((l,r))

sorted_LR = sorted(LR, key = lambda x: x[1])

ans = 0
x = 0

for l,r in sorted_LR:
    if x < l:
        ans += 1
        x = r + D - 1
print(ans)