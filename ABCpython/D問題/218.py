N = int(input())
points = []

from collections import defaultdict
p_exist = defaultdict(int)

for i in range(N):
    x,y = map(int,input().split())
    points.append([x,y])
    p_exist[(x,y)] = 1

ans = 0

for p1 in range(N):
    for p2 in range(p1 + 1, N):
        p1_x,p1_y = points[p1]
        p2_x,p2_y = points[p2]

        if p1_x == p2_x or p1_y == p2_y:
            continue

        if p_exist[(p1_x,p2_y)] == 1 and p_exist[(p2_x,p1_y)] == 1:
            ans += 1

    
ans //= 2

print(ans)