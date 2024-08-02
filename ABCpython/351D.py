from collections import deque

h, w = map(int, input().split())
field = [input() for _ in range(h)]

ans = 1
check = [[False] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if field[i][j] == "#" or check[i][j] or any(
                field[a][b] == "#" for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] if
                0 <= a < h and 0 <= b < w):
            continue
        q = deque()
        q.append([i, j])
        searched = {(i, j)}
        while q:
            x, y = q.popleft()
            mag = False
            for x_i, y_i in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= x_i < h and 0 <= y_i < w:
                    mag |= field[x_i][y_i] == "#"
            if not mag:
                check[x][y] = True
                for x_i, y_i in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= x_i < h and 0 <= y_i < w:
                        if (x_i, y_i) not in searched:
                            searched.add((x_i, y_i))
                            q.append([x_i, y_i])

        ans = max(ans, len(searched))

print(ans)
