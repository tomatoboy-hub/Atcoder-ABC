N = int(input())
L = [0] * N
R = [0] * N
for i in range(N):
    L[i], R[i] = map(int,input().split())
if sum(L) > 0 or sum(R) < 0:
    print("No")
    exit()

X = L.copy()
sum_X = sum(X)
for i in range(N):
    d = min((R[i] - L[i]) , -sum_X)
    sum_X += d
    X[i] += d

print("Yes")
print(*X)