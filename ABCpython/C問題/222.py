N,M = map(int,input().split())
A = []
for _ in range(N):
    A.append(list(map(str,input().split())))

player = [[0,i] for i in range(N)]


def winner(p1,p2):
    if p1 == p2:
        return "Aiko"
    elif (p1 == "G" and p2 == "C") or (p1 == "C" and p2 == "P") or (p1 == "P" and p2 == "G"):
        return "p1"
    else:
        return "p2"

for j in range(M):
    for k in range(0, N // 2, 2):
        player.sort()
        p1 = A[k][j]
        p2 = A[k+1][j]
        win = winner(p1,p2)
        if win == "p1":
            player[k][0] += 1
        elif win == "p2":
            player[k][0] += 1

for i in range(M):
    print(player[i][1])
