S = input()

ans = 0
for j in range(10000):
    flag = [False] * 10
    now = j
    for i in range(4):
       flag[now % 10] = True
       now //= 10
    flag2 = True
    for i in range(10):
        if S[i] == 'o' and flag[i] == False:
            flag2 = False
        if S[i] == 'x' and flag[i] == True:
            flag2 = False
    ans += flag2

print(ans)