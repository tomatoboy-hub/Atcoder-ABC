from typing import List
class UnionFind():
    def __init__(self,n):
        self.n = n  
        self.parent = [-1] * n
        self.__group_count = n

    def unite(self,x,y) -> bool:
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        
        self.__group_count -= 1
        if self.parent[x] > self.parent[y]:
            x,y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True
    def is_same(self,x,y) -> bool:
        return self.root(x) == self.root(y)
    
    def root(self,x) -> int:
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
    
    def size(self,x) -> int:
        return -self.parent[self.root(x)]
    def all_size(self) -> List[int]:
        sizes = []
        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes
    def groups(self) -> List[List[int]]:
        groups = dict()
        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)
        return list(groups.values())
    
    @property
    def group_count(self) -> int:
        return self.__group_count
N,M = map(int,input().split())

uf = UnionFind(N)
C = [0] * N
for _ in range(M):
    a,b = map(int,input().split())
    a,b = a - 1, b -1 
    if uf.is_same(a,b):
        print("No")
    uf.unite(a,b)
    C[a] += 1
    C[b] += 1
    for i in range(N):
        if C[i] >= 3:
            print("No")
print("Yes")

