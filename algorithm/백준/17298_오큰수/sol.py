import sys
sys.stdin = open("input.txt","r")

N = int(input())
A = list(map(int,input().split()))

# 오큰수는 오른족에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수 
# A = [3,5,2,7]  -> 5 7 7 1
# [9,5,4,8] -> -1 8 8 -1
NGE = [0] * N

stack = [A[N-1]]

for i in range(N-2,-1,-1):
    while stack:
        if stack[-1] > A[i]:
            NGE[i] = stack[-1]
            break
        else:
            stack.pop()

    if stack:
        stack.append(A[i])
    else:
        stack.append(A[i])
        NGE[i] = -1

NGE[N-1] = -1

print( *NGE )
