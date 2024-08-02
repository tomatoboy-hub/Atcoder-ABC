import heapq
N = int(input())
G = [[] for _ in range(N+1)]

for i in range(1,N):
    a,b,x = map(int,input().split())
    G[i].append((i + 1,a))
    G[i].append((x,b))

que = []
heapq.heapify(que)
INF = 1 << 60
dist= [INF] * (N + 1)
dist[1] = 0
heapq.heappush(que,(0,1))

while que:
    p = heapq.heappop(que)
    now = p[1]
    if dist[now] < p[0]:
        continue
    for next_v in G[now]:
        if dist[next_v[0]] > dist[now] + next_v[1]:
            dist[next_v[0]] = dist[now] + next_v[1]
            heapq.heappush(que,(dist[next_v[0]], next_v[0]))

print(dist[N])