from collections import deque
N, M = map(int,input().split())
edges = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * N
count = [0] * N
dist = [0] * N
count[0] = 1
visited[0] = True

deq = deque()
deq.append(0)

mod = 10 ** 9 + 7
while len(deq) > 0:
    v = deq.popleft()
    for nv in edges[v]:
        if visited[nv] == False:
            count[nv] = count[v]
            count[nv] %= mod
            dist[nv] = dist[v]+ 1
            visited[nv] = True
            deq.append(nv)
        else:
            if dist[nv] == dist[v] + 1:
                count[nv] += count[v]
                count[nv] %= mod

if visited[N-1] == False:
    print(0)
else:
    print(count[N-1])