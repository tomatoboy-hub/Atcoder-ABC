N = int(input())
A = list(map(int,input().split()))

stack = []
for i in range(N):
    if (i == 0):
        stack.append(A[i])
        continue
    stack.append(A[i])
    while True:
        if len(stack) == 1: break
        if stack[-1] != stack[-2]: break
        if (stack[-1] == stack[-2]):
            add = stack[-1] + 1
            stack.pop()
            stack.pop()
            stack.append(add)
    
print(len(stack))
