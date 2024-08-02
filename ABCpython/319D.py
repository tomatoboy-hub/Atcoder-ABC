N,M = map(int,input().split())
L = list(map(int,input().split()))

max_L = max(L)

def is_ok(x):
    if x < max_L:
        return False
    now_width = 1<<63
    cnt = 0
    for l in L:
        if now_width + l + 1 > x:
            cnt += 1
            now_width = l
        else:
            now_width += l + 1

    return cnt <= M

ok = 1<<63
ng = 0

while ok-ng > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)