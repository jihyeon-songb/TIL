import sys
sys.stdin = open('input.txt','r')

N, K= map(int, input().split())

result_list = []
check = [0]*(N+1)

for i in range(2,N+1):
    for j in range(i,N+1,i):
        if check[j]==False:
            result_list.append(j)
            check[j] = True 

print(result_list[K-1])