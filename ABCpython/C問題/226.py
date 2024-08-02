
N = int(input())
T = []
K = []
A = []
for i in range(N):
    sks = list(map(int,input().split()))
    T.append(sks[0])
    K.append(sks[1])
    if sks[1] != 0:
        A.append(sks[2:])
    else:
        A.append([])

requires = set(A[N-1])

get_skills = set()
ans = T[N-1]
while len(requires) > 0:
    skill = requires.pop()
    if skill not in get_skills:
        get_skills.add(skill)
        ans += T[skill-1]
        requires |= set(A[skill - 1])
print(ans)