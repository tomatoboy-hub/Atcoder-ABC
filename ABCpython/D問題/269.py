N = int(input())
Grid = [[0] * 3000 for i in range(3000)]

Start = []

for i in range(N):
    X,Y = map(int ,input().split())
    X += 1000
    Y += 1000

    Grid[X][Y] = 1
    Start.append([X,Y])

visited = [[False] * 3000 for i in range(3000)]

from collections import deque
que = deque()

ans = 0

for X,Y in Start:
    if visited[X][Y] == 0:
        que.append([X,Y])
        visited[X][Y] = 1
        ans += 1
        while len(que) > 0:
            NowX,NowY = que.popleft()
            if Grid[NowX-1][NowY-1] == 1 and visited[NowX-1][NowY-1] == 0:
                visited[NowX-1][NowY-1] = 1
                que.append([NowX-1,NowY-1])
            if Grid[NowX-1][NowY]==1 and visited[NowX-1][NowY]==0:
                visited[NowX-1][NowY]=1
                que.append([NowX-1,NowY])
            if Grid[NowX][NowY-1]==1 and visited[NowX][NowY-1]==0:
                visited[NowX][NowY-1]=1
                que.append([NowX,NowY-1])
            if Grid[NowX][NowY+1]==1 and visited[NowX][NowY+1]==0:
                visited[NowX][NowY+1]=1
                que.append([NowX,NowY+1])
            if Grid[NowX+1][NowY]==1 and visited[NowX+1][NowY]==0:
                visited[NowX+1][NowY]=1
                que.append([NowX+1,NowY])
            if Grid[NowX+1][NowY+1]==1 and visited[NowX+1][NowY+1]==0:
                visited[NowX+1][NowY+1]=1
                que.append([NowX+1,NowY+1])
        
print(ans)