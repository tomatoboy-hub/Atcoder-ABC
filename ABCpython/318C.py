# 入力の受け取り
N,D,P=map(int, input().split())
F=list(map(int, input().split()))

# 大きい順に並び替え
F.sort(reverse=True)

# 支払金額
pay=0

# 初期値
i=0
# D*i<Nの間
while D*i<N:
    # Pと(FのD*i～(D*(i+1)-1)までの和)のうち小さい方を足す
    pay+=min(P,sum(F[D*i:D*(i+1)]))
    # 次のiへ
    i+=1

# 答えの出力
print(pay)
    