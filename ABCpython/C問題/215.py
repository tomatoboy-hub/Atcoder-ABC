import itertools

S,K = map(str,input().split())
K = int(K)

S_set = set()

for seq in itertools.permutations(range(len(S))):
    S_tmp = ""
    for i in seq:
        S_tmp += S[i]
    S_set.add(S_tmp)

S_list = list(S_set)
S_list.sort()
print(S_list[K-1])
