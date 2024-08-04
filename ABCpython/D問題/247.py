from collections import deque
Q = int(input())

que = deque()


for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        que.append([query[1],query[2]])
    else:
        ans = 0
        c = query[1]
        while c > 0:
            number,p = que[0]
            if p >= c:
                p -= c
                ans += number * c
                que[0][1] = p
                c = 0
            else:
                ans += number * p
                que.popleft()
                c -= p
        print(ans) 
