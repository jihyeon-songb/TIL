import sys
sys.stdin = open("input.txt","r")

T = int(input())

arr = [[0]*300 for _ in range(300)]

value = 1
xy = 1

while True:
    for j in range(xy,0,-1):
        temp = (xy+1) - j
        arr[j][temp] = value
        value += 1
    xy += 1

    if xy == 300:
        break
    
    

for tc in range(1,T+1):
    p, q = map(int, input().split())

    x = 0
    y = 0
    count = 0

    while True:
        for i in range(1,300):
            for j in range(1,300):
                if arr[i][j] == p or arr[i][j] == q:
                    x += i
                    y += j
                    count += 1
                if count == 2:
                    break
                
        if count == 2:
            break

    result = arr[x][y]
    print("#{} {}".format(tc,result))

