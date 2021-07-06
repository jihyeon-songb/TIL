import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
# 상 좌 하 우
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    move = [[0,1,2,3],[0,2],[1,3],[0,3],[2,3],[1,2],[0,1]]
    possible = [[1,2,5,6],[1,3,4,5],[1,2,4,7],[1,3,6,7]]

    dq = deque()
    dq.append([R,C,1])
    visited[R][C] = 1
    count = 1
    while dq:
        r,c,d = dq.popleft()
        if d == L:
            break
        else:
            for i in move[arr[r][c]-1]:
                nr = r + dx[i]
                nc = c + dy[i]
                check = 0
                if nr >= N or nc >= M or nr < 0 or nc < 0:continue
                for j in possible[i]:
                    if arr[nr][nc] == j:
                        check = 1
                if visited[nr][nc] == 0 and check == 1:
                    visited[nr][nc] = 1
                    count += 1
                    dq.append([nr,nc,d+1])

    print("{} {}".format(tc,count))

