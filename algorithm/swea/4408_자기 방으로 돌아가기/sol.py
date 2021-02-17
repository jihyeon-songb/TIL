import sys
sys.stdin = open("input.txt","r")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [0] * 401

    for i in range(N):
        now ,later = map(int,input().split())
        if now > later:
            now, later = later, now

        if now % 2 == 0:
            now -= 1
        if later % 2:
            later += 1

        for j in range(now,later+1):
            arr[j] += 1
    
    max_value = 0

    for i in range(401):
        if max_value < arr[i]:
            max_value = arr[i]
    
    print("#{} {}".format(tc,max_value))





