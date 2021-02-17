import sys
sys.stdin = open('input.txt','r')

T = int(input())

def SetQueen(arr, r, N):
    global result 
    if r == N:
        result += 1
    else:
        for c in range(N):
            check = True
            for i in range(r):

                if arr[i][c] == 1:
                    check = False

                nc =  i-(r-c)
                if arr[i][nc] == 1 and nc >=0:
                    check = False

                nc = (r+c) - i
                if nc >= N: continue
                if arr[i][nc] == 1:
                    check = False

            if check:
                arr[r][c] = 1
                SetQueen(arr,r+1,N)
                arr[r][c] = 0


for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    result = 0
    SetQueen(arr,0,N)

    print("#{} {}".format(tc,result))