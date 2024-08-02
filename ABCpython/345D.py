def find_first_empty_position() -> tuple[int,int]:
    for i in range(H):
        for j in range(W):
            if not grid[i][j]:
                return i,j
    return -1,-1


def can_place_tile(h:int, w: int, a: int ,b : int) -> bool:
    if h + a > H or w + b > W:
        return False
    for i in range(h,h+a):
        for j in range(w,w + b):
            if grid[i][j] != 0:
                return False
    return True

def place_tile(h: int, w: int, a: int, b: int, val: int) -> None:
    for i in range(h, h + a):
        for j in range(w, w + b):
            grid[i][j] = val


def dfs(S) -> None:
    h,w = find_first_empty_position()
    if h == w == -1:
        print("Yes")
        exit()
    
    for idx in S:
        a,b = tiles[idx]
        for da,db in [(a,b),(b,a)]:
            if can_place_tile(h,w,da,db):
                place_tile(h,w,da,db,1)
                dfs(S - {idx})
                place_tile(h,w,da,db,0)

N,H,W = map(int,input().split())
tiles = [tuple(map(int,input().split())) for _ in range(N)]

grid = [[0] * W for _ in range(H)]
S = set(range(N))
dfs(S)

print("No")