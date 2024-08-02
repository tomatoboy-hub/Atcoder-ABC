N = int(input())
A = [0] + list(map(int,input().split()))

mae = {}
usiro = {}

for i in range (len(A) - 1):
    usiro[A[i]] = A[i + 1]
    mae[A[i + 1]] = A[i]

Q = int(input())
for _ in range(Q):
    t, *p = map(int,input().split())
    if t == 1:
        a,x = p
        b = usiro[a]
        mae[x] = a
        usiro[x] = b
        mae[b] = x
    else:
        x = p[0]
        mae[usiro[x]] = mae[x]
        usiro[mae[x]] = usiro[x]
        del mae[x]
        del usiro[x]

ans = []
crr = usiro[0]

while crr != 0:
    ans.append(crr)
    crr = usiro[crr]

print(*ans)