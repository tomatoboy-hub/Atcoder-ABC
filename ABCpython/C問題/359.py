sx,sy = map(int ,input().split())
gx,gy = map(int,input().split())

if sx > gx:
    sx,sy, gx,gy = gx,gy ,sx,sy

if sy > gy:
    gy = (gy - sy) * (-1) + sy

if sy % 2 == sx % 2:
    sx += 1

cost = 0

dy = gy - sy
cost += dy
sx = min(sx + dy,gx)
dx = gx - sx
cost += (dx + 1) // 2

print(cost)