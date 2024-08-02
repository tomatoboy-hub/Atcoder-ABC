from collections import defaultdict
N = int(input())

B_dict = defaultdict()

beans = []
for _ in range(N):
    a,c = map(int,input().split())
    beans.append([a,c])

for b in beans:
    if b[1] not in B_dict:
        B_dict[b[1]] = b[0]
    elif B_dict[b[1]] > b[0]:
        B_dict[b[1]] = b[0] 

max_min = -10**8
for b in B_dict.values():
     max_min = max(max_min, b)

print(max_min)
