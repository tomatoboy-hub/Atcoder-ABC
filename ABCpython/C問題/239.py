d = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

x1,y1,x2,y2 = map(int,input().split())
points1 = set()
points2 = set()
for (dx,dy) in d:
    print(dx,dy)
    points1.add((x1 + dx, y1 + dy))
    points2.add((x2 + dx, y2 + dy))

for point in points1:
    if point in points2:
        print("Yes")
        exit()

print("No")