import sys

# 高速な入力を受け取るための設定
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    
    # 配列Aを初期化
    A = [i for i in range(1, N + 1)]
    
    # 配列の先頭のずれを記録する変数
    shift = 0

    for _ in range(Q):
        query = list(map(int, input().split()))
        q_type = query[0]

        if q_type == 1:
            # タイプ1: 値の変更
            p, x = query[1], query[2]
            # 見た目上のp番目が、実際の配列のどのインデックスに対応するか計算
            actual_index = (p - 1 + shift) % N
            A[actual_index] = x
            
        elif q_type == 2:
            # タイプ2: 値の出力
            p = query[1]
            # 見た目上のp番目が、実際の配列のどのインデックスに対応するか計算
            actual_index = (p - 1 + shift) % N
            print(A[actual_index])
            
        elif q_type == 3:
            # タイプ3: 回転
            k = query[1]
            # 配列を実際に動かさず、ずれ(shift)だけを更新
            shift = (shift + k) % N

if __name__ == "__main__":
    main()