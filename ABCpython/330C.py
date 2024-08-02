D = int(input())
ans = D
for x in range(int(D**0.5) + 9):
    C = x * x - D
    if C > 0:
        ans = min(ans,C)
    else:
        y1 = int(C ** 0.5)
        y2 = -1 * y1        
        ans = min(ans,C + y1,)