N = int(input())

N3 = pow(3,N)

ans = [["."] * N3 for _ in range(N3)]

def f(i,j,N3):
    if N3 == 1:
        ans[i][j] = "#"
    else:
        N3 //= 3
        for ii in range(3):
            for jj in range(3):
                if ii == 1 and jj == 1: continue
                f(i + N3 * ii, j + N3*jj, N3)
    
f(0,0,N3)
for row in ans:
    print("".join(row))
    