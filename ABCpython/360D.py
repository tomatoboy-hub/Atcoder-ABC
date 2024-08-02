import bisect

N,T = map(int,input().split())

S = input()
X =list(map(int,input().split()))
L = []
toL = []
toR = []
for i in range(N):
    if S[i] == "0":
        toL.append(X[i])
    else:
        toR.append(X[i])


toL.sort()
result = 0
for e in toR:
    result += bisect.bisect_right(toL,e + 2 * T) - bisect.bisect_left(toL,e)

print(result)
