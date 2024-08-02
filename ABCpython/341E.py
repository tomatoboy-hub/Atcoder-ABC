N,Q = map(int,input().split())
S = input()
queries = []

for _ in range(Q):
    query = tuple(map(int,input().split()))
    queries.append(query)    
# flip配列を初期化
flip = [False] * N

# クエリを処理する関数
def process_queries(N, Q, S, queries):
    results = []  # クエリ2の結果を格納するリスト
    for q in queries:
        type, L, R = q
        L -= 1  # インデックス調整
        if type == 1:
            # クエリ1: LからRまでのflipを反転
            for i in range(L, R):
                flip[i] = not flip[i]
        else:
            # クエリ2: 良い文字列か判断
            good = True
            prev = None
            for i in range(L, R):
                char = S[i]
                if flip[i]:  # 反転が必要なら反転
                    char = '0' if char == '1' else '1'
                if prev is not None and prev == char:  # 連続する文字が同じなら良い文字列でない
                    good = False
                    break
                prev = char
            results.append("Yes" if good else "No")
    return results

# クエリを処理し、結果を出力
result = process_queries(N, Q, S,queries)
for i in result:
    print(i)