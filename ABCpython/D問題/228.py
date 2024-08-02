N = 2 ** 20
Q = int(input())
A = [-1] * N
P = list(range(N))

for _ in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        h = x % N
        pos = h
        visited = [pos]
        while A[pos] != -1:
            pos = P[pos]
            visited.append(pos)
        A[pos] = x
        new_p = P[(pos + 1) % N]
        for u in visited:
            P[u] = new_p

    else:
        print(A[x % N])