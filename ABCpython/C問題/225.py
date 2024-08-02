N,M = map(int,input().split())
B = []
for _ in range(N):
    B.append(list(map(int,input().split())))

def judge():

    for col in range(M):
        if B[0][col] % 7 == 0 and col != M-1:
            return False
    for row in range(N):
        for col in range(M -1 ):
            if B[row][col] + 1 != B[row][col + 1]:
                return False
    for row in range(N - 1):
        if B[row][0] + 7 != B[row + 1][0]:
            return False
    return True


print("Yes" if judge() else "No")