from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    while q:
        oi,oj = q.popleft()
        for ni,nj in neighbor8:
            if not seen[ni][nj] and S[ni][nj] == "#":
                seen[ni][nj] = True
                q.append((ni,nj))

def neighbor8(i,j):
    lst = []
    for di in [-1,0,1]:
        for dj in [-1,0,1]:
            if di == 0 and dj == 0:
                continue
            if 0 <= i+di < H and 0 <= j+dj < W:
                lst.append((i+di,j+dj))
    return lst
H,W = map(int,input().split())
S = [input() for _ in range(H)]
seen = [[False]*W for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if not seen[i][j] and S[i][j] == "#":
            seen[i][j] = True
            bfs(i,j)
            ans += 1

print(ans)