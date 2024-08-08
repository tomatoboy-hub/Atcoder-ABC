H,W, rs, cs = map(int,input().split())
N = int(input())

from collections import defaultdict
KabeDR = defaultdict(list)
KabeDC = defaultdict(list)

RC = []
CR = []

for i in range(N):
    r,c = map(int,input().split())
    RC.append([r,c])
    CR.append([c,r])

RC.sort()
CR.sort()

for r,c in RC:
    KabeDC[c].append(r)

for c,r in CR:
    KabeDR[r].append(c)

def NibutanR(NowR,NowC):
    if len(KabeDR[NowR]) == 0:
        return W + 1
    elif KabeDR[NowR][-1] < NowC:
        return W + 1
    elif NowC < KabeDR[NowR][0]:
        return KabeDR[NowR][0]
    l = 0
    r = len(KabeDR[NowR]) -1
    while 1 < r -l :
        c = (l + r) // 2

        if KabeDR[NowR][c] < NowC:
            l = c
        else:
            r = c
    return KabeDR[NowR][r]


