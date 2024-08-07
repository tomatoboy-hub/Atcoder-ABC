S = input()
dict = {x:i for i,x in enumerate("atcoder")}
R = []
for s in S:
    R.append(dict[s])
lens = len(S)
ans = 0
for i in range(lens):
    for j in range(lens-1, i, -1):
        if R[j] < R[j-1]:
            t = R[j]
            R[j] = R[j-1]
            R[j-1] = t 
            ans += 1
print(ans)