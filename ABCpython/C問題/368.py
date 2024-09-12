N = int(input())
H = list(map(int,input().split()))

T = 0
for h in H:
    while T % 3 != 0 and h > 0:
        T += 1
        if T % 3 == 0:
            h -=3
        else:
            h -= 1

    if h > 0:
        x = h // 5
        T += x * 3
        h %= 5

    while h > 0:
        T += 1
        if T % 3 == 0:
            h -= 3
        else:
            h -= 1

print(T)
