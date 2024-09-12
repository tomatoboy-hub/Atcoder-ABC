from collections import defaultdict

dic = defaultdict(list)

N = int(input())
for i in range(1,N+1):
    s,t = map(str,input().split())
    t = int(t)
    if len(dic[s]) != 0:
        continue
    dic[s] = [t,i]
ans = 0
idx = -1
for t in dic.values():
    if ans < t[0]:
        ans = t[0]
        idx = t[1]
print(idx)
