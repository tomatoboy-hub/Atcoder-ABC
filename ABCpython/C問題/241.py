N = int(input())
S = [[1 if c == "#" else 0 for c in input()] for _ in range(N)]


def judge(sr,sc,dr,dc):
    row,col = sr,sc
    bl = 0
    for _ in range(6):
        if not(0 <= row < N and 0 <= col < N):
            return False
        bl += S[row][col]
        row += dr
        col += dc
    return bl >= 4

pat = [(1,0),(0,1),(1,-1),(1,1)]
for i in range(N):
    for j in range(N):
        for dr,dc in pat:
            if judge(i,j,dr,dc):
                print("Yes")
                exit()
print("No")