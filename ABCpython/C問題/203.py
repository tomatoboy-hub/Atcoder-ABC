N,K = map(int,input().split())

d = []
for i in range(N):
    a,b = map(int,input().split())
    d.append((a,b))

d.sort()
now = K
for i in range(N):
    a,b = d[i]
    if now >= a:
        now += b
    else:
        break
print(now)
