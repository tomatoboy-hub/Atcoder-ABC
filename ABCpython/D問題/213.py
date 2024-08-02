import sys
sys.setrecursionlimit(10 ** 6)

def dfs(u,p):
    ans.append(u)
    for v in edge[u]:
        if v != p:
            dfs(v,u)
            ans.append(u)
    
N = int(input())

edge = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

for i in range(N+1):
    edge[i].sort()

ans = []
dfs(1,-1)
print(*ans)
