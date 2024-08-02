import bisect
N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [A[i] - (i + 1) for i in range(N)]  # A[i]未満で使える整数は、A[i] - (i+1）個

for _ in range(Q):
    K = int(input())
    i = bisect.bisect_left(S, K)
    if i == 0:
        print(K)
    else:
        print(A[i - 1] + (K - S[i - 1]))