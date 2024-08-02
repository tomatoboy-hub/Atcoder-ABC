from math import gcd
from math import lcm


def find_kth_num(N,M,K):
    left = 0
    right = 10 ** 20
    common = lcm(N,M)
    while (right > left ):
        mid = (left + right ) // 2
        count = mid // N + mid // M - 2 *(mid // common)

        if K <= count:
            right = mid
        else:
            left = mid + 1
    return left

N,M,K = map(int,input().split())         

print(find_kth_num(N,M,K))