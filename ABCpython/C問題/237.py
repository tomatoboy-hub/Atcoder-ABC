def judge():
    S = input()
    l = len(S) - len(S.lstrip("a"))
    r = len(S) - len(S.rstrip("a"))
    if l > r:return False
    T = "a" * (r - l) + S
    return T == T[::-1]
print("Yes" if judge() else "No")