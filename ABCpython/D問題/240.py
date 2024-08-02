N = int(input())
A = list(map(int,input().split()))

L = [(-1,0)]
ans = 0
for a in A:
    ans += 1
    k,num = L[-1]
    if a == k:
        L[-1][1] += 1
    else:
        L.append([a,1])
    if k == L[-1][1]:
        L.pop()
        ans -= k
    print(ans)

