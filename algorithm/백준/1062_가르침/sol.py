import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())

arr = list(input() for _ in range(N))
counting = [[0,0] for _ in range(26)]

for i in range(N):
    arr[i] = set(arr[i])
    for j in arr[i]:
        counting[ord(j)-97][0] += 1
        counting[ord(j)-97][1] = ord(j)-97

counting.sort(reverse=True)
result = set()
for i in range(K):
    result.add(chr(counting[i][1]+97))

count = 0
for i in arr:
    if (i - result) == set():
        count += 1

print(count)