from itertools import permutations
N,M = map(int,input().split())

AB = [[False] * N for _ in range(N)]
CD = [[False] * N for _ in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    AB[a][b] = True
    AB[b][a] = True

for _ in range(M):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    CD[c][d] = True
    CD[d][c] = True

def is_same_shape(P):
    for i in range(N):
        for j in range(N):
            if AB[P[i]][P[j]] != CD[i][j] : return False
    return True

for perm in permutations(range(N)):
    if is_same_shape(perm):
        print("Yes")
print("No")