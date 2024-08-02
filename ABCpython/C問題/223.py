N = int(input())
L = []
sec = 0

for _ in range(N):
    a,b = map(int,input().split())
    L.append((a,b))
    sec += a/b
rem = sec / 2

ans = 0
for a,b in L:
    if rem >= a / b:
        ans += a
        rem -= a / b
    else:
        ans += rem * b
        break
print(ans)