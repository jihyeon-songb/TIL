import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def move(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= R or ny >= C: continue
        if arr[nx][ny] == 'S':
            return 0
        elif arr[nx][ny] == '.':
            arr[nx][ny] = 'D'
    return 1

for tc in range(1,T+1):
    R,C = map(int,input().split())

    arr = [list(input()) for _ in range(R)]
    result = 1
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'W':
                result = move(i,j)
    
    if result:
        print(result)
        for i in range(R):
            for j in range(C):
                print(arr[i][j],end='')
            print()
    else:
        print(result)