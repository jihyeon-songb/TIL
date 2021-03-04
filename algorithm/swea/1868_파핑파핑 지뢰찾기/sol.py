import sys
sys.stdin = open('input.txt')

T = int(input())
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [0, 1, -1, 1, -1, 0, 1, -1]

def zero(i,j):
    check = 1
    for k in range(8):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx<0 or ny<0 or nx>=N or ny>=N:continue
        if arr[nx][ny] == '*':
            check = 0
            return check
    return check

for tc in range(1,T+1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]
    
    stack_x = []
    stack_y = []
    visited = [[0]*(N) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            check = 0
            if visited[i][j] == 0 and arr[i][j] != '*':
                check = zero(i,j)
            if check:
                stack_x.append(i)
                stack_y.append(j)
                while stack_x and stack_y:
                    x = stack_x.pop()
                    y = stack_y.pop()
                    visited[x][y] = 1
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx<0 or ny<0 or nx>=N or ny>=N:continue
                        if visited[nx][ny] == 0:
                            if zero(nx,ny):
                                stack_x.append(nx)
                                stack_y.append(ny)
                            else:
                                visited[nx][ny] = 1
                result += 1
    print(arr)   
    print(visited)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '*':continue
            if visited[i][j] == 0:
                result += 1 
    
    print("#{} {}".format(tc,result))