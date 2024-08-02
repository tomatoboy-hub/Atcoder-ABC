from itertools import permutations
from math import factorial
n,k = map(int,input().split())
s = input()
if len(set(s)) == 10:
    print(factorial (10))
    exit()
ans = 0

for t in set(permutations(s)):
    for i in range(n - k + 1):
        u = t[i: i + k]
        if u == u[::-1]:
            break
    else:
        ans += 1

print(ans)