N,A,B = map(int,input().split())
D = list(map(int,input().split()))
INF = 10 ** 11
min_day = INF
max_day = -INF
for i in range(N):
    v = D[i] % (A+B)
    if v == 0:
        v = (A+B)
    min_day = min(min_day,v)
    max_day = max(max_day,v)

print("Yes" if (max_day - min_day) < A else "No")