N = int(input())
A = list(map(int,input().split()))
sum_A = sum(A)
X = int(input())

ans = 0
ans += X // sum_A

X %= sum_A
i = 0
while X >= 0:
    X -= A[i]
    i += 1

print(ans*len(A) + i)
