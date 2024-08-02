from collections import Counter
N,K = map(int,input().split())
C = list(map(int,input().split()))


counter = Counter(C[:K])

ans = len(counter)
for i in range(K,N):
    left = C[i - K]
    right = C[i]
    counter[left] -= 1
    counter[right] += 1
    if counter[left] == 0:
        del counter[left]
    ans = max(ans,len(counter))
print(ans)