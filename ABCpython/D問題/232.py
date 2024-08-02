from collections import deque
H,W = map(int,input().split())
C= [input() for _ in range(H)]
dist = [[0] * W for _ in range(H)]


d = [(0,1),(1,0)]
que = deque()
que.append((0,0))
dist[0][0] = 1 
while len(que) > 0:
    x,y = que.popleft()
    now = dist[x][y]
    for _x, _y in d:
        nx, ny = x + _x, y + _y
        if nx < H and ny < W and C[nx][ny] != "#":
            dist[nx][ny] =now + 1
            que.append((nx,ny))

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, dist[i][j])

print(ans)