N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
count = 0
ans = 0
for a in A:
    if count <= M-1 and B[count] <= a:
        count += 1
        ans += a


print(ans) if count == M else print(-1)