from heapq import heappush, heappop

n = int(input())
data = []
for _ in range(n):
    t,d = map(int,input().split())
    data.append((t, t + d))

data.sort()
print("data",data)
last = 0
ans = 0
q = []
i = 0
while True:
    while i < n and data[i][0] <= last + 1:
        heappush(q,data[i][1])
        print("q",q)
        i += 1

    if q:
        x = heappop(q)
        if last + 1 <= x:
            ans += 1
            last += 1
    elif i < n:
        last = data[i][0] - 1
    else:
        break
    print("last",last)
print(ans)