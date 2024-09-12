N,K = map(int,input().split())
edges = [set() for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edges[a].add(b)
    edges[b].add(a)

V = set(list(map(lambda x: int(x) - 1, input().split())))


"""
葉をVの中にないものから一つずつ消していきつつ
len(edges[i]) == 1のものを削除候補に加えていく
"""
from collections import deque
mono = deque()
count = 0
for i in range(N):
    if len(edges[i]) <= 1 and i not in V:
        count += 1
        mono.append(i)


while len(mono) > 0:
    m = mono.popleft()
    if m not in V:
        for next_v in edges[m]:
            edges[next_v].remove(m)
            if len(edges[next_v]) <= 1 and next_v not in V:
                count += 1
                mono.append(next_v)

print(N - count)


    
