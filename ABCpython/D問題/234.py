N,K = map(int,input().split())
P = list(map(int,input().split()))

import heapq

pq = P[:K]
heapq.heapify(pq)

print(pq[0]) 

for x in P[K:]:
    heapq.heappush(pq,x)
    heapq.heappop(pq)
    print(pq[0])