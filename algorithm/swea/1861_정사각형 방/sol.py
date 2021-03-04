import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 첫 시작 부분만 뽑아서 이동해보자!

# 첫 사작이 될 수 있는지 알아보기
def Pass(i,j):
    count = 0
    check = 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
        if arr[nx][ny] == arr[i][j] - 1:
            count += 1
            check = 0
        elif arr[nx][ny] == arr[i][j] + 1:
            count += 1
    # 주변에 자신보다 1큰 값, 1작은 값 둘다 있는 값과 
    # 1큰 값만 있는 것은 False
    if count == 2 or check == 0:
        return False
    # 주변에 자신보다 1큰 값만 있거나 1큰 값. 1작은 값 둘다 없는 값만 True 
    else:
        return True

# 첫 시작부터 끝까지 움직이기
def Move(i,j,visited):
    dq = deque()
    dq.append((i,j))
    visited[i][j] = 1
    count = 1
    while dq:
        x,y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:continue
            if arr[nx][ny] == arr[x][y] + 1:
                dq.append((nx,ny))
                count += 1
                visited[nx][ny] = 1
    
    return [arr[i][j],count]

for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * (N+1) for _ in range(N+1)]

    max_move = 0
    start_idx = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                # 첫 시작이라면
                if Pass(i,j):
                    start, count = Move(i,j,visited)
                    if max_move < count:
                        start_idx = start
                        max_move = count
                    elif max_move == count:
                        if start_idx > start:
                            start_idx = start
    
    print('#{} {} {}'.format(tc, start_idx, max_move))



