import itertools


M = int(input())
S1 = input()
S2 = input()
S3 = input()
INF = 10 ** 9 + 7
ans = INF
for i in range(M):
    for j in range(M):
        for k in range(M):
            if not (S1[i] == S2[j] == S3[k]):
                continue
            now_ans = 0
            count = [0] * M
            for m in (i,j,k):
                now_ans = max(now_ans,m+count[m]*M)
                count[m] += 1
            ans = min(ans,now_ans)

if ans == INF:
    print(-1)
else:
    print(ans)