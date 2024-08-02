N = int(input())
l = [0] * N
r = [0] * N

for i in range(N):
    l[i],r[i] = map(int,input().split())

l.sort()
r.sort()

ans = N * (N - 1) // 2
j = 0
for i in range(N):
    while r[j] < l[i]:
        j += 1
    ans -= j

print(ans)