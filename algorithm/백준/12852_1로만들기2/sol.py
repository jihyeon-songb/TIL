import sys
sys.stdin = open('input.txt')

N = int(input())

DP = [0]*(N+1)

for i in range(2,N+1):
    DP[i] = DP[i-1]+1
    if i%2==0:
        DP[i] = min(DP[i],DP[i//2]+1)
    if i%3==0:
        DP[i] = min(DP[i],DP[i//3]+1)

i = DP[N]
j = N
result_list = [N]

# 결과 리스트 찾기
while i:
    i -= 1
    if DP[j-1] == i:
        j -= 1
        result_list.append(j)
        continue
    elif j%2==0 and DP[j//2]==i:
        j //= 2
        result_list.append(j)
        continue
    elif j%3 ==0 and DP[j//3]==i:
        j //= 3
        result_list.append(j)
        continue

print(DP[N])
print(*result_list)
