# O(N)解法の例
# この解法は、DPの考え方を文字列操作に適用したものです

def solve():
    N = int(input())
    S = input()

    if N <= 1:
        print(S)
        return

    # dp[i] は S[i:] に対する答え
    # 後ろから計算する
    dp = [""] * N
    dp[N-1] = S[N-1]

    for i in range(N - 2, -1, -1):
        # Case 1: S[i]を動かさない場合
        # この場合、答えのプレフィックスはS[i]で、残りはS[i+1:]の最適解
        cand1 = S[i] + dp[i+1]

        # Case 2: S[i]を動かす場合
        # この場合、S[i+1]が先頭に来る。S[i]をどこに挿入するのがベストか？
        # S[i]とdp[i+1]を比較する
        if S[i] < dp[i+1]:
            # S[i]の方が小さいなら、S[i]を前に持ってくるべき（つまり動かさない）
            # なので、cand1がこのケースを包含している
            cand2 = cand1
        else: # S[i] >= dp[i+1]
            # S[i]を動かした方が良い可能性がある
            # 実際には、S[i]をdp[i+1]の中に挿入して最小の文字列を作る
            # しかし、単純にS[i]とdp[i+1]を入れ替えた文字列と比較するだけで十分
            cand2 = dp[i+1] + S[i]
        
        dp[i] = min(cand1, cand2)

    print(dp[0])

# --- メインの実行部分 ---
T = int(input())
for _ in range(T):
    solve()