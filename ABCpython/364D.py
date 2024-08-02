import sys
import bisect

N,Q = map(int,input().split())
A = list(map(int,input().split()))

queries = []
for j in range(Q):
    b,k = map(int,input().split())
    queries.append((b, k))

# Sort A
A.sort()

results = []
for b, k in queries:
    # Calculate distances and sort
    distances = []
    for a in A:
        distance = abs(a - b)
        distances.append(distance)
    
    distances.sort()
    result = distances[k - 1]
    results.append(result)

for result in results:
    print(result)

