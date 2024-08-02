H,W,N = map(int,input().split())

T = input()

S = [input() for _ in range(H)]
count = 0
flag = True
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            flag = True
            I = i
            J = j
            for k in T:
                if k == "R":
                    J += 1
                if k == "L":
                    J -= 1
                if k == "U":
                    I -=1
                if k == "D":
                    I += 1
                if S[I][J] == "#":
                    flag = False
                    break
            if flag == True: count += 1

print(count)