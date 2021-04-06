import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split()))

arr.sort()

result = 0
temp = 0
for i in range(N):
    temp = temp + arr[i]
    result += temp

print(result)