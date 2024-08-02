S = input()
K = int(input())
from collections import deque

que = deque()
remain = K
score = 0 
ans = 0
for char in S:
    score += 1
    if char == ".":
        que.append(1)
        remain -= 1
    else:
        que.append(0)
    while remain < 0:
        remain += que.popleft()
        score -= 1
    ans = max(ans, score)
print(ans)