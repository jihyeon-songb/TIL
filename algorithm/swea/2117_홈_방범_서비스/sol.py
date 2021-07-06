import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1,T+1):
    N, M = list(map(int,input().split()))
    city = [ list(map(int,input().split())) for _ in range(N) ]

    count = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                count += 1
    
    cost = count * M
    K = 1
    while True:
        if cost < K*K + (K-1)*(K-1):
            break
        K += 1
    
    result = 0
    for u in range(1,K):
        cost = u*u + (u-1)*(u-1)
        for i in range(N):
            for j in range(N):
                temp = 0
                total = 0
                for k in range(i-u+1,i+u):
                    for s in range(j-temp,j+temp+1):
                        if k<0 or s<0 or k>=N or s>=N: continue
                        if city[k][s] == 1:
                            total += 1   
                    if k < i:
                        temp += 1
                    else:
                        temp -= 1
                if cost <= total*M:
                    result = max(result,total)
    
    print("#{} {}".format(tc, result))