from itertools import accumulate

N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

cumsumA = [0]+ A + [L]

def check(x):
    offset = 0
    temp = 0
    cnt = 0
    for i in range(len(cumsumA)):
        if cumsumA[i] - cumsumA[offset] >= x:
            offset = i
            cnt += 1
    if cnt > K:
        return True
    else:
        return False

left = 0
right = L

while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
    
print(left)