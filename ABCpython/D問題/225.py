N,Q = map(int,input().split())

_next = [-1] * (N + 1)
_prev = [-1] * (N + 1)

for _ in range(Q):
    query = list(map(int,input().split()))
    q = query[0]
    if q == 1:
        x,y = query[1:]
        _next[x] = y
        _prev[y] = x
    elif q == 2:
        x,y = query[1:]
        _next[x] = -1
        _prev[y] = -1
    else:
        x = query[1]
        ans = []
        curr = x
        while _prev[curr] != -1:
            curr = _prev[curr]
        while curr != -1:
            ans.append(curr)
            curr = _next[curr]
        
        print(len(ans),*ans)