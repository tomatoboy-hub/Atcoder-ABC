import bisect

N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
for _ in range(Q):
    b,k = map(int,input().split())
    """
    二分探索でBj + x のxを求めに行けばいいのか? 
    """
    left = -1
    right = 10 ** 9
    b_idx = bisect.bisect_left(A,b)
    while right - left > 1:
        mid = (left + right) // 2
        max_idx = bisect.bisect_right(A,b+mid)
        min_idx = bisect.bisect_left(A,b-mid)
        if (max_idx - min_idx) >= k:
            right= mid
        else:
            left = mid
    print(right)
    