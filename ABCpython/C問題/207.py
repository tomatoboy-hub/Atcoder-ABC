def func(t,l,r):
    if t == 1:
        return l,r
    if t == 2:
        return l , r - 0.5
    if t == 3:
        return l + 0.5, r
    if t == 4:
        return l + 0.5,r -0.5
def judge (a,b,c,d):
    b1 = b < c
    b2 = d < a
    if not (b1 or b2):
        return 1
    else:
        return 0
    
N = int(input())
L = [-1] * N
R = [-1] * N
for i in range(N):
    t,l,r = map(int,input().split())
    l,r = func(t,l,r)
    L[i],R[i] = l,r
ans = 0
for i in range(N):
    a,b = L[i],R[i]
    for j in range(i + 1, N):
        c,d = L[j],R[j]
        ans += judge(a,b,c,d)
print(ans)