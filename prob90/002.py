N = int(input())

if N % 2 != 0:
    exit()

temp = []
for i in range(1 << N):
    kakko = ""
    is_ok = 0
    for bit in format(i,"b"):
        if bit == "1":
            kakko += "("
            is_ok += 1
        else:
            kakko += ")"
            is_ok -= 1
        if is_ok < 0:
            break
    if is_ok == 0 and len(kakko) == N:
        temp.append(kakko)

temp.reverse()
print(*temp,sep="\n")