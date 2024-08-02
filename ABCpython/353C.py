
N = int(input())
A = list(map(int, input().split()))

# 10^8
MOD = 10**8

# Aを昇順にして，二分探索できるようにする．
A.sort()

# 和がMOD(10^8)を超えた回数を記録する変数．
cnt = 0

# Aを一つ一つ注目する．最後のAは注目しなくて良い．
for i in range(N-1):
  ## <めぐる式二分探索>
  l = i # 左端は注目しているAの位置
  r = N # 右端は一番右で良い
  while r-l>1:
    m = (l+r)//2
    
    # MOD(10^8)を和が超える境目を見ている．
    if(A[m]+A[i]>=MOD):
      r = m
    else:
      l = m
  ## </めぐる式二分探索>
  
  # 和がMOD(10^8)を超えた回数を記録する．
  cnt += N-r

# 総和のN-1倍から，MOD(10^8)を超えた回数とMOD(10^8)の積を引いて出力
print(sum(A)*(N-1)-(cnt*MOD))