import sys 
sys.setrecursionlimit(10 ** 6)
N = int(input())
# メモ化再帰
from functools import lru_cache
@lru_cache()
def f(k):
    if k == 0:
        return 1
    return f(k // 2) + f(k // 3)

print(f(N))