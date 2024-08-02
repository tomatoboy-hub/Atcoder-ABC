from heapq import heappush,heappop
N,A,B,C = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(N)]

que = []
dist = [1 << 60] * (N*2)
heappush(que,(0,0))
dist[0] = 0

while que:
    time,city = heappop(que)
    if dist[city] < time:
        continue
    if city < N:
        for next_city in range(N):
            next_time = dist[city] + D[city][next_city] * A
            if next_time < dist[next_city]:
                dist[next_city] = next_time
                heappush(que,(next_time,next_city))
    for next_city in range(N,N*2):
        next_time = dist[city] + D[city%N][next_city%N] * B + C
        if next_time < dist[next_city]:
            dist[next_city] = next_time
            heappush(que,(next_time,next_city))

print(min(dist[N-1],dist[N*2-1]))