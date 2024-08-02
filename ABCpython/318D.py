import sys
sys.setrecursionlimit(1000000)

N = int(input())
D = [[0] * (N+1)]

for i in range(1,N):
    d = list(map(int, input().split()))
    d = [0] * (i + 1) + D
    D.append(d)

D.append([0] * (N+1))

for i in range(1,N+1):
    for k in range(1,N+1):
        D[k][i] = D[i][k]

Used = [False] * (N+1)
Used[0] = True

Pair = []
ans = 0

def DFS(Used):
    global ans
    if all(Used):
        count = 0
        for i in range(0,N//2):
            count += D[Pair[2*i]][Pair[2*i+1]]
        ans = max(ans,count)
    
    else:
        x = Used.index(False)
        for k in range(x+1,N+1):
            if not Used[k]:
                Pair.append(x)
                Pair.append(k)
                Used[x] = True
                Used[k] = True
                DFS(Used)
                Pair.pop()
                Pair.pop()
                Used[x] = False
                Used[k] = False

if N % 2 == 0:
    DFS(Used)
else:
    for i in range(1,N+1):
        Used[i] = True
        DFS(Used)
        Used[i] = False

print(ans)