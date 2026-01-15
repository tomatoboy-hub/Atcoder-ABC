from collections import deque

N = int(input())

edges = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)


def bfs(start):
    dq = deque()
    dq.append(start)
    dist = [-1] * N
    dist[start] = 0
    max_dist = [start,0]
    while dq:
        v = dq.popleft()
        for next_v in edges[v]:
            if dist[next_v] == -1:
                dist[next_v] = dist[v] + 1
                dq.append(next_v)
                if dist[next_v] > max_dist[1]:
                    max_dist = [next_v,dist[next_v]]
    return max_dist

mid_point,mid_dist = bfs(0)
final_point, final_dist = bfs(mid_point)
print(final_dist + 1)