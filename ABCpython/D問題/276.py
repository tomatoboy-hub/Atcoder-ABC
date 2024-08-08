# 入力の受け取り
N=int(input())
A=list(map(int,input().split()))

# ai=2^x*3^y*z (x,y,z)の記録
xyz=[]

# i=0~(N-1)
for i in range(N):
    # xのカウント
    x=0
    # A[i]が2で割り切れる限り
    # ⇔2で割った余りが0
    while A[i]%2==0:
        # xをカウント
        x+=1
        # 2で割る
        A[i]//=2

    # yのカウント
    y=0
    # A[i]が3で割り切れる限り
    # ⇔3で割った余りが0
    while A[i]%3==0:
        # yをカウント
        y+=1
        # 3で割る
        A[i]//=3

    # 記録
    xyz.append([x,y,A[i]])

# zが同一か確認
# i=1~(N-1)
for i in range(1,N):
    # a0のz≠aiのz　ならば
    if xyz[0][2]!=xyz[i][2]:
        # 「-1」を出力
        print(-1)
        # 終了
        exit()

# xの最小
xmin=9999
# yの最小
ymin=9999

# i=0~(N-1)
for i in range(N):
    # より小さければ更新
    xmin=min(xmin,xyz[i][0])
    ymin=min(ymin,xyz[i][1])

# 答え
ans=0

# i=0~(N-1)
for i in range(N):
    # 操作回数=xと(xの最小)との差
    ans+=xyz[i][0]-xmin
    # 操作回数=yと(yの最小)との差
    ans+=xyz[i][1]-ymin

# 答えの出力
print(ans)
