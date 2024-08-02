import heapq
N,M = map(int,input().split())
A = list(map(int,input().split()))
edges = [[] for _ in range(N)]
for i in range(M):
    u,v,b = map(int,input().split())
    u -= 1
    v -= 1
    edges[u].append((v, b + A[v]))
    edges[v].append([u, b + A[u]])

que = []

INF = 10 << 60
dist = [INF] * N
dist[0] = A[0]

heapq.heappush(que, (A[0], 0))

while que:
    p = heapq.heappop(que)
    now = p[1]
    if dist[now] < p[0]:
        continue

    for next_v in edges[now]:
        isf dist[next_v[0]] > dist[now] + next_v[1]:
         x   dist[next_v[0]] = dist[now] + next_v[1]
            heapq.heappush(que,(dist[next_v[0]], next_v[0]))
    
print(*dist[1:])