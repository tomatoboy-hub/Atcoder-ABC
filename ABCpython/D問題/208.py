N,M = map(int,input().split())

INF = 1 << 60

edges = [[INF] * N for _ in range(N)]
for i in range(N):
    edges[i][i] = 0

for _ in range(M):
    x,y,z = map(int,input().split())
    edges[x-1][y-1] = z

def warshall_floyd(N):
    ans = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                edges[i][j] = min(edges[i][j],edges[i][k] + edges[k][j])
                if edges[i][j] != INF:
                    ans += edges[i][j]
    return ans

print(warshall_floyd(N))