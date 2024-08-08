N,x,y = map(int,input().split())
A = [0] + list(map(int,input().split()))
Sx = set()
Sy = set()

Sx.add(A[1])
Sy.add(0)

for i in range(2, N + 1):
    if i % 2 == 0:
        NewSy = set()
        for yi in Sy:
            NewSy.add(yi - A[i])
            NewSy.add(yi + A[i])
        Sy = NewSy
    
    else:
        NewSx = set()
        for xi in Sx:
            NewSx.add(xi - A[i])
            NewSx.add(xi + A[i])

        Sx = NewSx
# xがSxにある かつ yがSyにある
if x in Sx and y in Sy:
    # 「Yes」を出力
    print("Yes")
# そうでなければ
else:
    # 「No」を出力
    print("No")