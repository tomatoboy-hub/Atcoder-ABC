from heapq import heappop,heappush 
def max_pop(q):
    a = heappop(q)
    a[0] *= -1
    return  a

def max_push(q,x):
    x[0] *= -1
    heappush(q,x)

h,w = map(int,input().split())
field = [input() for _ in range(h)]
sx,sy,gx,gy = 0,0,0,0
for i, a in enumerate(field):
    for j, a_j in enumerate(a):
        if a_j == "S":
            sx,sy = i,j
        if a_j == "T":
            gx,gy = i,j
    
n = int(input())
d = [[0] * w for _ in range(h)]

for _ in range(n):
    r_i,c_i,e_i = map(int,input().split())
    d[r_i - 1][c_i - 1] = e_i

q = list()
q.append([0,sx,sy])
E = [[-1] * w for _ in range(h)]
while q:
    e_i ,x, y = max_pop(q)
    if E[x][y] > e_i:
        continue
    if e_i < d[x][y]:
        e_i = d[x][y]
        E[x][y] = e_i
    if e_i == 0:
        continue

    for x_i,y_i in [(x + 1,y),(x - 1, y), (x, y + 1),(x, y - 1)]:
        if 0 <= x_i < h and 0 <= y_i < w and field[x_i][y_i] != "#" and E[x_i][y_i] < e_i - 1:
            E[x_i][y_i] = e_i - 1
            max_push(q,[e_i - 1, x_i,y_i])

print("Yes" if E[gx][gy] >= 0 else "No")