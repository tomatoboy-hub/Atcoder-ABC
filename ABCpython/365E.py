def calculate_xor_sum(N, A):
    # 累積XOR配列の初期化
    X = [0] * (N + 1)
    
    # 累積XORの計算
    for k in range(1, N + 1):
        X[k] = X[k - 1] ^ A[k - 1]
    
    result = 0
    
    # 各要素の寄与を計算
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            result += X[j] ^ X[i - 1]
    
    return result

# 入力例
N = int(input())
A = list(map(int,input().split()))
# 結果の計算と出力
result = calculate_xor_sum(N, A)
print(result)  # 出力例: 83
