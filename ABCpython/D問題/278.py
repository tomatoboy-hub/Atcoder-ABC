N = int(input())
A = list(map(int,input().split()))
Q = int(input())
base = 0
plus = {i: A[i] for i in range(N)}
for _ in range(Q):
    query = list(map(int,input().split()))
    n = query[0]
    if n == 1:
        _,x = query
        base = x
        plus = {}
    elif n == 2:
        _,i,x = query
        i -= 1
        plus.setdefault(i, 0)
        plus[i] += x
    else:
        _,i = query
        i -= 1
        p = 0
        if i in plus:
            p = plus[i]
        print(base + p)
