import bisect
N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort(reverse= True)
B.sort(reverse = True)

cum_A = [0] * N
cum_B = [0] * N
cum_A[0] = A[0]
cum_B[0] = B[0]

for i in range(1,N):
    cum_A[i] = cum_A[i-1] + A[i]
    cum_B[i] = cum_B[i-1] + B[i]

sweet = 10 << 20
salty = 10 << 20
for i in range(N):
    if X < cum_A[i]:
        sweet = i+1
        break
    if Y < cum_B[i]:
        salty = i+1
        break
ans = min(sweet,salty)
print(min(ans, N))