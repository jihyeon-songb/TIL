import sys
sys.stdin = open('input.txt')

T = 1

def Cal(start_list,x,temp):
    for i in start_list:
        temp += (arr[i-1][x-1]+arr[x-1][i-1])
    return temp

def start_link(total,idx,c,start):
    global start_list
    global result_list
    if c == N//2:
        result_list += [total]
        return

    for i in range(idx,N+1):
        if visited[i] == 0:
            visited[i] = 1
            temp = Cal(start_list,i,0)
            total += temp
            start_list += [i]
            start_link(total,i+1,c+1,start_list)
            start_list.remove(i)
            visited[i] =0
            total -= temp

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*(N+1)
    result_list= []
    start_list = []
    start_link(0,1,0,start_list)
    j = len(result_list)-1
    min_value = 987654321
    for i in range(len(result_list)//2):
        x = abs(result_list[i]-result_list[j])
        min_value = min(min_value,x)
        j-= 1
    print(result_list)
    print(min_value)
