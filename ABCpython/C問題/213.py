H,W,N = map(int,input().split())
R = []
C = []
for _ in range(N):
    r,c = map(int,input().split())
    R.append(r)
    C.append(c)

Rs = sorted(set(R))
Cs = sorted(set(C))

Rd = {x:i for i,x in enumerate(Rs,1)}
Cd = {x:i for i,x in enumerate(Cs,1)}

for r,c in zip(R,C):
    print(Rd[r],Cd[c])
