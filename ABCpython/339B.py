N = int(input())
A = list(map(int,input().split()))
ST = []
for i in range(N-1):
    s,t = map(int,input().split())
    ST.append((s,t))
def max_currency_exchange(N, A, ST):
    # Aは各国の通貨の初期値、STは各国間の交換レートと獲得単位のリスト
    
    for i in range(N-1):
        # Si単位以上持っている場合にのみ交換可能
        Si, Ti = ST[i]
        # 可能な限り交換
        exchanges = min(A[i] // Si, (A[i] - A[i] % Si) // Si)
        A[i] -= exchanges * Si
        A[i+1] += exchanges * Ti
    
    return A[-1]

# 入力例


# 最終的に国Nの通貨の単位数としてあり得る最大値を計算
max_currency = max_currency_exchange(N, A, ST)
print(max_currency)