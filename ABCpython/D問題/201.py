H,W = map(int,input().split())

grid = []

for _ in range(H):
    _s = input()
    r = [1 if char == "+" else -1 for char in _s]
    grid.append(r)

INF = float("INF")
dp_first = [[0] * W for _ in range(H)]
dp_second = [[0] * W for _ in range(H)]


for row in reversed(range(H)):
    for col in reversed(range(W)):
        if row == H -1 and col == W - 1:
            continue
        s1,s2 = - INF, -INF
        if row + 1 < H:
            s1 = dp_second[row + 1][col] + grid[row + 1][col]
        if col + 1 < W:
            s2 = dp_second[row][col + 1] + grid[row][col + 1]
        dp_first[row][col] = max(s1,s2)

        s1,s2 = INF, INF
        if row + 1 < H:
            s1 = dp_first[row + 1][col] - grid[row + 1][col]
        if col + 1 < W:
            s2 = dp_first[row][col + 1] - grid[row][col + 1]
        dp_second[row][col] = min(s1,s2)
    
x = dp_first[0][0]

if x == 0:
    print("Draw")
elif x > 0:
    print("Takahashi")
else:
    print("Aoki")