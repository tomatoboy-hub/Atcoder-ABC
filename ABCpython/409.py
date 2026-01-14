def solve():
    N = int(input())
    S = input()
    ans = S
    for l in range(N):  
        change = S[l]
        best_r_for_l = -1
        best_S_for_l = S 
        for r in range(l, N):
            prefix = S[:l]
            sub = S[l:r+1]
            suffix = S[r+1:]
            shifted_sub = sub[1:] + sub[0]
            current_S = prefix + shifted_sub + suffix
            if current_S < best_S_for_l:
                best_S_for_l = current_S
        
        if best_S_for_l < ans:
            ans = best_S_for_l

    print(ans)


T = int(input())
for _ in range(T):
    solve()