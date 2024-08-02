import sys
import pypyjit

sys.setrecursionlimit(10 ** 7)
pypyjit.set_param('max_unroll_recursion=-1')

def size(v,par):
    result = 1
    for ch in edges[v]:
        if ch == par:
            continue
        result += size(ch,v)
    return result

N = int(input())

edges = []

for _ in range(N - 1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)


P = []
for v in edges[0]:
    P.append(size(v,0))

ans = sum(P) - max(P) + 1
print(ans)