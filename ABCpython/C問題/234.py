K = int(input())
bit = format(K,'b')

ans = ""
for b in bit:
    if b == "1":
        ans += "2"
    else:
        ans += "0" 

print(ans) 