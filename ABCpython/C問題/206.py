from collections import Counter
N = int(input())
A = list(map(int,input().split()))

c = Counter(A)

ans = 0
for i in range(len(A)):
    ans += (N - i) - c[A[i]]
    c[A[i]] -= 1

print(ans)