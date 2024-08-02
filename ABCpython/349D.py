L,R = map(int,input().split())
ans = []

while (L < R):
    i = 0
    while ((L  % 2 ** i) == 0 and (L + 2 ** i) <= R):
        r = L + 2 ** i
        i += 1

    ans.append([L, r])
    L = r 

print(len(ans))
for a,b in ans:
    print(str(a) + " " + str(b))