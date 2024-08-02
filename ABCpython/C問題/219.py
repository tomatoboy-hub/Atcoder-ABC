X = input()
D = dict()

for i in range(26):
    nxt = chr(i + ord('a'))
    D[X[i]] = nxt

N = input()
A = []
for _ in range(N):
    S = input()
    T = ''
    for char in S:
        T += D[char]
    A.append((T,S))
A.sort()


for i in range(N):
    print(A[i][1])
    