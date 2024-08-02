N,M = map(int,input().split())
S = input()
T = input()

def can_stamp(left_idx):
    for el1,el2 in zip(S[left_idx:left_idx+M],T):
        if el1 not in ["#",el2]:
            return False
    return True

def stamp(left_idx):
    for dist in range(M):
        i = left_idx + dist
        if i >= N:
            break
        S[i] = "#"


seen = set()
stamp_stack = []
for i in range(N-M+1):
    if can_stamp(i):
        stamp_stack.append(i)
        seen.add(i)


while stamp_stack:
    idx = stamp_stack.pop()
    stamp(idx)
    for i in range(idx- M + 1,idx + M):
        if not 0 <= i < N-M+1:
            continue
        if can_stamp(i) and i not in seen:
            stamp_stack.append(i)
            seen.add(i)


for s in S:
    if s != "#":
        print("No")
        exit()

print("Yes")