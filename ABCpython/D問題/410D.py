import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a,b,w = map(int,input().split())
    a -= 1
    b -= 1
    edge[a].append((b,w))

went = set()
ans = float('inf')

def solve(next = 0, now = 0):
    global ans
    if next == N-1:
        ans = min(ans,now)
    if (next, now) in went:
        return None
    went.add((next,now))
    for b,w in edge[next]:
        result = solve(next = b, now = now ^ w)
        if result is not None:
            return result
    return None

solve()

if ans == float('inf'):
    print(-1)
else:
    print(ans)