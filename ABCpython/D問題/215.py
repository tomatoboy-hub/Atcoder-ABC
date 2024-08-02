N,M = map(int,input().split())
A = list(map(int,input().split()))

def prime_factorize(x):
    if x == 1:
        return [1]
    prime_list = []
    i = 2

    while i * i <=x:
        if x % i == 0:
            prime_list.append(i)
            x //= i
        else:
            i += 1
    if x != 1:
        prime_list.append(x)
    return prime_list

prime_set = set()
for x in A:
    if x == 1:
        continue
    prime_x = prime_factorize(x)
    for p in prime_x:
        prime_set.add(p)
    
# ans_judge[x]=1なら答え、=0なら答えでない
ans_judge=[1]*(M+1)

# prime_set=Aの要素が持つ素数(p)について
for p in prime_set:
    # p*1,p*2,p*3,...,p*k,...は答えでない→ans_judge[p*k]=0とする
    # p*kがMを超えるまで
    k=1
    while p*k<=M:
        ans_judge[p*k]=0
        k+=1

# 答えの格納用リスト
ans=[]

# 1～Mまで
for i in range(1,M+1):
    # ans_judge[i]=1ならiは答え
    if ans_judge[i]==1:
        ans.append(i)

# 答えの個数を出力
print(len(ans))
# 答えを出力
for i in ans:
    print(i)