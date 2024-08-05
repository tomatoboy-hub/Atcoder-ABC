N,X = map(int,input().split())
AB = []
for _ in range(N):
    a,b = map(int,input().split())
    AB.append([a,b])
INF = 10 ** 10
ans = [INF] * N
temp = [0] * (N+1)
for i,(a,b) in enumerate(AB):
    if i > X -1 :
        continue
    ans[i] = temp[i] + a + b * (X - i)
    temp[i+1] = temp[i] + a+b

print(min(ans))