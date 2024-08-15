"""
Y軸方向には移動しないからY軸でCounterすればいいかな? 
Rで小さい Lで大きいものがないといけない
"""
N = int(input())
XY = []
for _ in range(N):
    x,y = map(int,input().split())
    XY.append([x,y])

S = input()
from collections import defaultdict
dic = defaultdict(list)
for i in range(N):
    x,y = XY[i]
    s = S[i]
    dic[y].append([x,s])

for items in dic.values():
    l = -1
    r = 10 ** 10
    for item in items:
        if item[0] == "L":
            l = max(l,item[0])
        if item[1] == "R":
            r = min(r,item[0])
    if r <= l:
        print("Yes")
        exit()
print("No")

