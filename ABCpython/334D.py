from bisect import bisect_right
N,Q = map(int,input().split())
R = list(map(int,input().split()))
query = []
for _ in range(Q):
    q = int(input())
    query.append(q)


R.sort()
cum_R = [0] * (N)
cum_R[0] = R[0]

for i in range(1, N):
    cum_R[i] = cum_R[i-1] + R[i] 


for q in query:
    index = bisect_right(cum_R,q)
    print(index)
