from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int,input().split()))

Q = int(input())
A.sort()
for _ in range(Q):
    B = int(input())
    ans = 0
    left = -1
    right = N

    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] < B:
            left = mid
        else:
            right = mid
    comp1 = 10 ** 9
    comp2 = 10 ** 9
    if left >= 0:
        comp1 = abs(A[left] - B)
    if left + 1 < N:
        comp2 = abs(A[left+1] - B)
    print(min(comp1, comp2))

