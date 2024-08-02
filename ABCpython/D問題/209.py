from collections import deque

N,Q = map(int,input().split())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

colors = [-1] * N
deq = deque()
deq.append(0)
colors[0] = 0
while len(deq) > 0:
    v = deq.popleft()
    color = colors[v]
    for nv in edges[v]:
        if colors[nv] != -1:
                continue
        elif color == 1:
            colors[nv] = 0
            deq.append(nv)
        else:
            colors[nv] = 1
            deq.append(nv)
for _ in range(Q):
     c,d = map(int,input().split())
     c -= 1
     d -= 1
     print("Town" if colors[c] == colors[d] else "Road")