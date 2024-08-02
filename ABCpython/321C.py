K = int(input())
numbers = []

for binary in range(2, 1 << 10):
    ans = ""
    for i in range(9,-1,-1):
        if (binary & (1 << i)) != 0:
            ans += str(i)
    numbers.append(ans)

numbers.sort()
print(numbers[K-1])