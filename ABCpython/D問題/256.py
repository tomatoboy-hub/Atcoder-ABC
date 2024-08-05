N = int(input())
LR = []
for _ in range(N):
    l,r = map(int,input().split())
    LR.append([l,r])

LR.sort()
NowL = LR[0][0]
NowR = LR[0][1]
for i in range(1, N):
    NextL = LR[i][0]
    NextR = LR[i][1]
    if NowR < NextL:
        print(NowL,NowR)
        NowL = NextL
        NowR = NextR
    else:
        if NowR < NextR:
            NowR = NextR
print(NowL,NowR)