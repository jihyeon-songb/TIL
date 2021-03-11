import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N,M = map(int,input().split())

visited = [[0]*N for _ in range(M)]
arr = [list(input()) for _ in range(M)]

WB = [ 0, 0]

dq = deque()

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            count = 0
            visited[i][j] = 1
            dq.append([i,j])
            while dq:
                x , y = dq.popleft()
                count += 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= M or ny >= N: continue
                    if visited[nx][ny] == 0 and arr[x][y] == arr[nx][ny]:
                        visited[nx][ny] = 1
                        dq.append([nx,ny])

            if arr[i][j] == 'W':
                WB[0] += count**2
            else:
                WB[1] += count**2

print(*WB)