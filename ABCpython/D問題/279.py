A,B = map(float,input().split())

if 2 * B - A >= 0:
    ans = A
else:
    minus= 1
    plus = 10 ** 15

    while plus - minus != 1:
        mid = (minus + plus ) // 2
        if 2 * B * mid ** 1.5 - A <= 0:
            minus = mid
        else:
            plus = mid
    
    ans = min(B * (minus -1 ) + A / (minus) ** 0.5, B * (plus - 1) + A/(plus ) ** 0.5)
print(ans)