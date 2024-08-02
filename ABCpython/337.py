n = int(input()) -1
lst = []

while n > 0:
    lst.append(n % 5)
    n //= 5

ans = 0
for l_i in reversed(lst):
    ans = ans * 10 + l_i * 2

print(ans)