def is_dag():
    L = []
    S = deque([i for i in range(N) if cnt[i] == 0])
    while S:
        u = S.popleft()
        L.append(u)
        for v in G[u]:
            cnt[v] -= 1
            if cnt[v] == 0:
                S.append(v)
    return all(x == 0 for x in cnt)

from collections import deque
N,M = map(int,input().split())

G = [[] for _ in range(N)]
cnt = [0] * N
for _ in range(M):
    k = int(input())
    A = list(map(int,input().split()))
    for i in range(k - 1):
        prv = A[i] - 1
        nxt = A[i + 1] - 1
        G[prv].append(nxt)
        cnt[nxt] += 1

if is_dag():
    print("Yes")
else:
    print("No")