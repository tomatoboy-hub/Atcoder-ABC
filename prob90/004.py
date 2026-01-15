H,W = map(int,input().split())

grid = []
for _ in range(H):
    A = list(map(int,input().split()))
    grid.append(A)

Hs = [0] * H
for i in range(H):
    Hs[i] = sum(grid[i])

Ws = [0] * W
for j in range(W):
    Ws[j] = sum(grid[i][j] for i in range(H))

for i in range(H):
    for j in range(W):
        print(Hs[i] + Ws[j] - grid[i][j], end=" ")
    print()