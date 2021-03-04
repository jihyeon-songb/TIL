import sys
sys.stdin = open('input.txt','r')

N = int(input())

def Hanoi(N, start, mid, end):
    if N == 0:
        return
    else:
        Hanoi(N-1,start,end,mid)
        print(start, end)
        Hanoi(N-1,mid,start,end)

result = 2**N-1
print(result)

if N <= 20:
    Hanoi(N,1,2,3)