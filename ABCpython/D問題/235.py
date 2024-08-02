a, N = map(int,input().split())
from collections import deque

INF = 1 << 62
MAX_N = 10 ** 6

dist = [INF] * MAX_N
dist[1] = 0
que = deque((1,))
while que:
    x = que.popleft()
    new_cost = dist[x] + 1
    nx1 = x * a
    if nx1 < MAX_N:
        if new_cost < dist[nx1]:
            dist[nx1] = new_cost
            que.append(nx1)
    if x % 10 != 0 and x >= 10:
        nx2 = int (str(x % 10) + str(x // 10))
        if new_cost < dist[nx2]:
            dist[nx2] = new_cost
            que.append(nx2)
if dist[N] != INF:
    print(dist[N])
else:
    print(-1)