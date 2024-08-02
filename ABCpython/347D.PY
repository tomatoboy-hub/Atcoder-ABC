a, b, C = map(int, input().split())
c = 0
for i in range(60):
    if (C >> i) & 1:
        c += 1
d = (a + b - c) // 2

wa = C.bit_count()


sa =  abs(b - a) 

x = (wa + sa) // 2
y = ( wa - sa ) // 2

if y < 0:
    print(-1)
    exit()

X = 0
Y = 0
for i in range(60):
    if (C >> i) & 1:
        if a > b:
            a -= 1
            X += 1 << i
        else:
            b -= 1
            Y += 1 << i
        c -= 1
    else:
        if a + b > c and a * b != 0:
            a -= 1
            b -= 1
            X += 1 << i
            Y += 1 << i
if a > 0 or b > 0:
    print(-1)
    exit()
print(X, Y)
