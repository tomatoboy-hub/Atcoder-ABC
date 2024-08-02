n,m,k = map(int,input().split())


tests = []

for _ in range(m):
    c, *a, r = input().split()
    tests.append((list(map(int, a)),r))

ans = 0

for bit in range(2 ** n):
    valid = True
    for a,r in tests:
        cnt = sum(bit >> (key - 1) for key in a)
        if (r == 'o' and cnt < k) or (r == 'x' and cnt >= k):
            valid = False
    if valid:
        ans += 1

print(ans)