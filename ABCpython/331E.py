N,M,L = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ng_set = set()

for _ in range(L):
    c,d = map(lambda x: int(x) - 1, input().split())
    ng_set.add((c,d))

p = sorted([(b,j) for j,b in enumerate(B)],reverse = True)

ans = -1

for i,a in enumerate(A):
    for b,j in p:
        if (i,j) not in ng_set:
            ans = max(ans,a+b)
            break
print(ans)