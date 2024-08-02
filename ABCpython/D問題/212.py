import heapq
Q = int(input())

que = []

S = 0

for _ in range(Q):
    q = list(map(int,input().split()))
    query = q[0]
    if query == 1:
        x = q[1]
        heapq.heappush(que,x - S)
    elif query == 2:
        x = q[1]
        S += x
    elif query == 3:
        y = heapq.heappop(que)
        print(y + S)

