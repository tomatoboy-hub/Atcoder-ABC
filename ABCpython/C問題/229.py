N,W = map(int,input().split())
cheese = []
for _ in range(N):
    a,b = map(int,input().split())
    cheese.append([a,b])

cheese.sort(reverse=True)
i = 0
ans = 0
while W > 0:
    if i == N:
        break
    if W - cheese[i][1] >= 0 :
        ans += cheese[i][0] * cheese[i][1]
        W -= cheese[i][1]
        i += 1
    else:
        ans += cheese[i][0] * W
        break

print(ans)