T = int(input())
for _ in range(T):
    N = int(input())
    S = input()

    l = -1
    for i in range(N-1):
        if S[i] > S[i+1]:
            l = i
            break
    if l == -1:
        print(S)
        continue
    r = N
    for j in range(l + 1, N):
        if S[l] < S[j]:
            r = j
            break
    print(S[:l] + S[l+1:r] + S[l] + S[r:])