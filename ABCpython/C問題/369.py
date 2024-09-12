N = int(input())
A = list(map(int,input().split()))

"""
階差数列をとって同じ値の数をカウントすればいいのかしら?? 
"""
B = []
for i in range(1, N):
    B.append(A[i]-A[i-1])
count = N
rensa = 1

for i in range(N-1):
    if i == N-2:
        count += rensa * (rensa + 1) * 2
    elif B[i+1] == B[i]:
        rensa += 1
    else:
        count += rensa * (rensa + 1) // 2
        rensa = 1

print(count)
