N,T,P = map(int,input().split())
L = list(map(int,input().split()))
L.sort()

if L[-P] >= T:
    print(0)
else:
    print(T - L[-P])
