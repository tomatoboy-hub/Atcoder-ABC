from bisect import bisect_left,bisect_right



N = int(input())
A = list(map(int,input().split()))
Q = int(input())
pos = [[] for _ in range(N+1)]

for i ,x in enumerate(A,1):
    pos[x].append(i)

for _ in range(Q):
    L,R,X = map(int,input().split())
    B = pos[X]
    print(bisect_right(B,R) - bisect_left(B,L))