from collections import deque

N,M=map(int,input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    A,B,X,Y = map(int,input().split())
    A-=1
    B-=1
    edge[A].append((B,X,Y))
    edge[B].append((A,-X,-Y))

que = deque()
que.append(0)
coord = [None] * N
coord[0] = (0,0)
while que:
    v = que.popleft()
    ox,oy = coord[v]
    for nv,x,y in edge[v]:
        if coord[nv] is not None:
            continue
        coord[nv] = [ox+x,oy+y]
        que.append(nv)

for i in range(N):
    if coord[i] is None:
        print("undecidable")
    else:
        print(*coord[i])