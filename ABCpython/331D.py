def f(r,c):
    qi,mi = divmod(r,N)
    qj,mj = divmod(c,N)
    result = (qi*qj) * P_sum
    result += P_acc[mi][N] * qj
    result += P_acc[N][mj] * qi
    result += P_acc[mi][mj]
    return result

N,Q = map(int,input().split())
P = [input() for _ in range(N)]
P_acc = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if P[i][j] == "B":
            P_acc[i+1][j+1] = 1

for i in range(1,N+1):
    for j in range(1,N+1):
        P_acc[i][j] += P_acc[i][j-1]

for j in range(1,N+1):
    for i in range(1,N+1):
        P_acc[i][j] += P_acc[i-1][j]
    
P_sum = P_acc[N][N]

for _ in range(Q):
    si,sj,gi,gj = map(int,input().split())
    gi,gj = gi + 1,gj+1
    ans = f(gi,gj) - f(gi,si) - f(si,gj) + f(si,sj)
    print(ans)