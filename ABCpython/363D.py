N = int(input())
L = len(str(N))

l = [1]
for i in range(18):
    l.append(l[-1] + 9*10 ** i)
    l.append(l[-1] + 9 * 10 ** i)

def loop(n):
    for i,v in enumerate(l):
        if v > N:
            n -= l[i-1]
            d = (i + 1) // 2
            half = 10 ** (d-1) + n-1
            ans = str(half)
            rev = ''.join(list(reversed(ans)))
            if i % 2 == 1:
                ans += rev[1:]
            else:
                ans += rev

            return ans
print(loop(N))