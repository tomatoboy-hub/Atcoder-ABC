import sys
sys.setrecursionlimit(10 ** 6)

N,M = map(int,input().split())
edges = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edges[a] = b
    edges[b] = a

seen = [False] * (N + 1)

def dfs(v):
    global edges, seen, this_group, this_group_e
    seen[v] = True
    this_group.add(v)
    this_group_e += len(edges[v])
    for next_v in edges[v]:
        if not seen[next_v]:
            dfs(next_v)

result = 0
for i in range(N):
    if not seen[i]:
        this_group = set()
        this_group_e = 0
        dfs(i)
        s = len(this_group)
        result += s * (s - 1)//2 - this_group_e // 2

print(result)
