from math import gcd

N = int(input())
XY = []
for _ in range(N):
    x,y = map(int,input().split())
    XY.append((x,y))
S = set()
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        xi,yi = XY[i]
        xj,yj = XY[j]
        xd,yd = xi - xj, yi - yj
        g = gcd(xd,yd)
        S.add((xd // g, yd // g))

print(len(S))