import itertools
N = int(input())

points = []
for i in range(N):
    x,y = map(int,input().split())
    points.append((x,y))

ans = 0
def triangle_area(p1, p2, p3):
    return abs(p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])) / 2

for seq in itertools.combinations(range(N),3):
    tmp_p = []
    for i in seq:
        tmp_p.append(points[i])
    triange =triangle_area(tmp_p[0], tmp_p[1], tmp_p[2])
    if triange > 0:
        ans += 1

print(ans)