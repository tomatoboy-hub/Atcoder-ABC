T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    flg = False
    flg2 = False
    ans = ""
    change = ""
    if N == 1:
        print(S)
        continue
    for i in range(1,N):
        if flg == False and S[i] < S[i-1]:
            flg = True
            change = S[i-1]
            ans += S[:i-1]
            point = i-1
            continue
        if flg == True and S[i] >= change:
            flg2 = True
            ans += S[point+1:i]
            ans += change
            ans += S[i:]
            continue
    if flg2 == False:
        ans += S[point+1:] + change
    print(ans)



