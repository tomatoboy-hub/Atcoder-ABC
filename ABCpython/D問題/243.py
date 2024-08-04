N,X = map(int,input().split())
S = input()
ans = X
up = 0
s = []
for i in range(N):
    if S[i] == "U" and len(s) > 0 and( s[-1] == "L" or s[-1] == "R"):
        s.pop()
    else:
        s.append(S[i])
for i in range(N):
    if s[i] == "U":
        ans //= 2
    elif s[i] == "L":
        ans = ans * 2
    else:
        ans = ans * 2 + 1

print(ans) 