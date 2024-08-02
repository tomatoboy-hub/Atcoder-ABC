from collections import defaultdict
N,T = map(int,input().split())
p = [0] * N
point = defaultdict(int)
point[0] = N
for i in range(T):
    a,b = map(int,input().split())
    a -= 1
    old = p[a]
    p[a] += b
    if point[old] == 1:
        del point[old]
    else:
        point[old] -= 1
    point[p[a]] += 1
    print(len(point))
