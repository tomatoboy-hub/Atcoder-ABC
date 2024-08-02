N = int(input())
A =list(map(int,input().split()))
W = list(map(int,input().split()))
edges = [[] for _ in range(N)]

for a,w in zip(A,W):
    a -= 1
    edges[a].append(w)
ans = 0
for edge in edges:
    if len(edge) >= 2:
        edge.sort(reverse = True)
        ans += (sum(edge[1:]))
print(ans)
