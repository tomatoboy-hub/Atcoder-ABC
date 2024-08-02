N,M = map(int,input().split())
count = [0] * (N + 1)
connect = [[] for _ in range(N+1)]

for i in range(M):
    A,B = map(int,input().split())
    connect[A].append(B)
    count[B] += 1


import heapq

que = []

for i in range(1, N+ 1):
    if count[i] == 0:
        que.append(i)

heapq.heapify(que)

ans = []
while len(que) >0 :
    now = heapq.heappop(que)
    ans.append(now)
    for to in connect[now]:
        count[to] -= 1
        if count[to] == 0:
            heapq.heappush(que,to)
        
if len(ans) == N:
    print(*ans)
else:
    print(-1)