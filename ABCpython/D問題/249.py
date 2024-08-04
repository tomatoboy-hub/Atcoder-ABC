from collections import Counter
N = int(input())
A = list(map(int,input().split()))

C = Counter(A)
ans = 0
A_max = 2 * 10 ** 5

for den in range(1, A_max + 1):
    for num in range(den,A_max + 1, den):
        k = num // den
        ans += C[den] * C[num] * C[k]
print(ans)