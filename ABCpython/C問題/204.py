import sys 
sys.setrecursionlimit(10 ** 6)
N,M = map(int,input().split())
edges = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edges[a].append(b)

def dfs(v,edges,visited):
    visited[v] = True
    for next_v in edges[v]:
        if visited[next_v] != True:
            dfs(next_v,edges,visited)

ans = 0
for i in range(N):
    visited = [False] * N
    dfs(i,edges,visited)
    ans += sum(visited)

print(ans)