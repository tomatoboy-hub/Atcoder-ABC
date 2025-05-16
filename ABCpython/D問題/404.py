from itertools import product

N, M = map(int, input().split())
C = list(map(int, input().split()))

# 各動物がどの動物園で見られるかの情報を入力
zoos = [[] for _ in range(N)]
for i in range(M):
    data = list(map(int, input().split()))
    for zoo in data[1:]:
        zoos[zoo - 1].append(i)
ans = 10 ** 20
"""
# 各動物園を0回, 1回, 2回訪れる組み合わせを生成
for visits in product(range(3), repeat=N):
    seen = [0] * M
    temp = 0
    for i, visit_count in enumerate(visits):
        for _ in range(visit_count):
            for animal in zoos[i]:
                seen[animal] += 1
        temp += C[i] * visit_count
    # すべての動物が2回以上見られるか確認

    if all(count >= 2 for count in seen):
        ans = min(ans, temp)
"""
comb_list = []
v = []
def dfs(v):
    global comb_list
    if len(v) == N:
        print(v)
        comb_list.append(v.copy())

        return 
    for i in range(3):
        v.append(i)
        dfs(v)
        v.pop()
dfs(v)


for visits in comb_list:
    seen = [0] * M
    temp = 0
    for i, visit_count in enumerate(visits):
        for _ in range(visit_count):
            for animal in zoos[i]:
                seen[animal] += 1
        temp += C[i] * visit_count
    if all(count >= 2 for count in seen):
        ans = min(ans, temp)
        

print(ans)