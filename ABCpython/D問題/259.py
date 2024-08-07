# pypyで提出

# UnionFind
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n
 
    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
 
    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return 
 
    def same(self,a,b):
        return self.leader(a) == self.leader(b)
 
    def size(self,a):
        return abs(self.parent_size[self.leader(a)])
 
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

# 入力の受け取り
N=int(input())
sx,sy,tx,ty=map(int,input().split())

# 円の情報
p=[]

# N回
for i in range(N):
    # 入力の受け取り
    x,y,r=map(int,input().split())
    # 記録
    p.append([x,y,r])

# UnionFindを用意
UF=UnionFind(N)

# i=0~(N-1)
for i in range(N):
    # k=(i+1)~(N-1)
    for k in range(i+1,N):
        # 座標と半径を取り出し
        ix,iy,ir=p[i]
        kx,ky,kr=p[k]

        # 中心間距離の二乗
        d=(ix-kx)**2+(iy-ky)**2

        # 外接
        if d==(ir+kr)**2:
            # 円iと円kは「乗り換え可能」
            # ⇔連結
            UF.merge(i, k)
        # 2点で交わる
        elif (ir-kr)**2<d<(ir+kr)**2:
            UF.merge(i, k)
        # 内接
        elif d==(ir-kr)**2:
            UF.merge(i, k)

# スタートの点が載っている円
Start=[]
# ゴールの点が載っている円
Goal=[]

# i=0~(N-1)
for i in range(N):
    # 中心、半径の取り出し
    ix,iy,ir=p[i]

    # スタートの点が円周上にあれば
    if (sx-ix)**2+(sy-iy)**2==ir**2:
        # 記録
        Start.append(i)
    # ゴールの点が円周上にあれば
    if (tx-ix)**2+(ty-iy)**2==ir**2:
        # 記録
        Goal.append(i)
# x：スタートの点が載っている円
for x in Start:
    # y：ゴールの点が載っている円
    for y in Goal:
        # 連結なら
        if UF.same(x,y):
            # 「Yes」を出力
            print("Yes")
            # 終了
            exit()

# 「No」を出力
print("No")
