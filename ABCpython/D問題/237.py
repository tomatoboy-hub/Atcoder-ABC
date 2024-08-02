from collections import deque
N = int(input())
S = input()

ans = deque((N,))
for i in reversed(range(N)):
    if S[i] == "L":
        ans.append(i)
    else:
        ans.appendleft(i)
print(*ans)