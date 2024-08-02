N, K = map(int,input().split())
P = []
for _ in range(N):
    p = list(map(int,input().split()))
    P.append(sum(p))

sorted_p = sorted(P,reverse=True)
for i in range(N):
    if P[i] >= sorted_p[K-1]:
        print("Yes")
    elif P[i] + 300 >= sorted_p[K-1]:
        print("Yes")
    else:
        print("No")