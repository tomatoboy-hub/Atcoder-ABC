def simulate_grid(H, W, N):
    # グリッドの初期化（全て白で）
    grid = [['.' for _ in range(W)] for _ in range(H)]
    
    # 高橋君の初期位置と向き（上を向いている）
    x, y = 0, 0  # 0-indexedで管理
    direction = 0  # 0:上, 1:右, 2:下, 3:左
    
    # 方向に応じた移動量（dx, dy）
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for _ in range(N):
        # 現在のマスの色に応じて操作
        if grid[x][y] == '.':
            # 白なら黒に塗り、時計回りに90度回転
            grid[x][y] = '#'
            direction = (direction + 1) % 4
        else:
            # 黒なら白に塗り、反時計回りに90度回転
            grid[x][y] = '.'
            direction = (direction - 1) % 4
        
        # 次のマスへ移動
        x = (x + dx[direction]) % H
        y = (y + dy[direction]) % W
    
    return grid

# 入力例
H, W, N = map(int,input().split())
final_grid = simulate_grid(H, W, N)

# 最終グリッドの出力
for row in final_grid:
    print(''.join(row))
