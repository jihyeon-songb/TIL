import sys
sys.stdin = open('input.txt','r')

T = int(input())

def SetQueen(arr, r, N, result):
    if r == N:
        result += 1
    for c in range(N):
        arr[r][c] = 1
        for i in range(r):
            pass

    
for tc in range(1,T+1):
    N = int(input())
    
    arr = [[0]*N for _ in range(N)]