N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())

H = Q - P + 1
W = S - R + 1

for i in range(P,Q + 1):
    ans = []
    for j in range(R, S+ 1):
        if(i - j ==  A - B) or (i + j  == A + B):
            ans.append("#")
        else:
            ans.append(".")
    print(*ans,sep="") 