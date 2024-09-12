import queue 
def com(N):
    return N * (N-1) / 2

WHITE, BLACK  = 0,1

N,M = map(int,input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    G[v].append(v)
    G[u].append(v)

num_ng_edges = 0
is_bipartite = True
color = [-1] * N

for s in range(N):
    if color[s] != -1 :continue
    white_num, black_num = 0,0
    que = queue.Queue()
    que.put(s)
    color[s] = WHITE
    while not que.empty():
        v = que.get()
        if color[v] == WHITE: white_num += 1
        else: black_num += 1
        for v2 in G[v]:
            if color[v2] != -1:
                if color[v2] == color[v]:
                    is_bipartite = False
            else:
                color[v2] = 1 - color[v]
                que.put(v2)
    num_ng_edges += com(white_num) + com(black_num)

print(com(N) - M - num_ng_edges if is_bipartite else 0)