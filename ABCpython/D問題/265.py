from itertools import accumulate
N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))
acc_A2 = [0] + list(accumulate(A))
acc_A = set(accumulate(A))
for a in acc_A2:
    p_,q_,r_ = a + P, a + P + Q, a + P + Q + R
    if p_ in acc_A and q_ in acc_A and r_ in acc_A:
        print("Yes")
        exit()
print("No")