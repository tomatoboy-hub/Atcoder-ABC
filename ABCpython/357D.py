N = int(input()) # 入力
mod = 998244353 # mod
L = len(str(N)) # 桁数
a = N%mod # 初項
r = pow(10, L, mod) # 等比
nu = a*(pow(r, N, mod)-1) # V_Nの分子
de = r-1 # V_Nの分母
invDe = pow(de, -1, mod) # V_Nの分母の逆数
ans = (nu*invDe)%mod # 答え
print(ans)
