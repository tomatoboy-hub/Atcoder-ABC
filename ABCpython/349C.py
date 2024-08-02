S = input().upper()
T = input()
if T[2] == "X":
    T = T[:2]
    """
    dp[i][j] = Tのi文字目 , Sのj文字目までを利用したときにときに何文字共通しているか
    """
    dp = [[0] * (len(S) + 1) for _ in range(len(T) + 1)]
    for i in range(len(T)):
        for j in range(len(S)):
            if (T[i] == S[j]):
                dp[i+1][j + 1] = max(dp[i][j] + 1,dp[i+1][j+1])
            else:
                dp[i+1][j+1] = max(dp[i][j + 1], dp[i+1][j],dp[i+1][j+1])


    print("Yes" if dp[len(T)][len(S)] >= 2 else "No")
else:
    """
    dp[i][j] = Tのi文字目 , Sのj文字目までを利用したときにときに何文字共通しているか
    """
    dp = [[0] * (len(S) + 1) for _ in range(len(T) + 1)]
    for i in range(len(T)):
        for j in range(len(S)):
            if (T[i] == S[j]):
                dp[i+1][j + 1] = max(dp[i][j] + 1,dp[i+1][j+1])
            else:
                dp[i+1][j+1] = max(dp[i][j + 1], dp[i+1][j],dp[i+1][j+1])


    print("Yes" if dp[len(T)][len(S)] >= 3 else "No")
