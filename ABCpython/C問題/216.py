N = int(input())

ans = []
while N > 0:
    if N % 2 == 0:
        ans.append("B")
        N //= 2
    else:
        ans.append("A")
        N -= 1
ans.reverse()
print("".join(ans))
print(len(ans))
    