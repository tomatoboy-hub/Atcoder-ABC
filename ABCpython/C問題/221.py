import itertools

N = input()

ans = 0

for seq in itertools.permutations(range(len(N))):
    s_tmp = ""
    for i in seq:
        s_tmp += N[i]    
    for i in range(1,len(N)):
        if not (s_tmp[0] == "0" or s_tmp[i] == "0"): 
            ans = max(ans, int(s_tmp[:i]) * int(s_tmp[i:]))

print(ans)