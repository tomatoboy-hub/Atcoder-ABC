from bisect import bisect_left
N,M,P = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

B.sort()
B_sum = [0]
for b in B:
    B_sum.append(B_sum[-1] + b)
ans = 0
for a in A:
    if a > P:
        ans += P*M
    else:  
        ans += a 
        k = bisect_left(B,P-a)
        ans += B_sum[k]
        ans += (M-k) * (P-a)

print(ans)