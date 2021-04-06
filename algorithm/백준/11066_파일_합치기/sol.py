import sys
sys.stdin = open('input.txt')

T=int(input())

def add(arr):
    for i in range(K):
        for j in range(i,K):
            if i%2:
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            else:
                if arr[i] > arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
    result_list = []
    for i in range(1,K,2):
        result_list.append(arr[i]+arr[i-1])
    if len(arr)%2:
        result_list.append(arr[len(arr)-1])
    if len(result_list)==1:
        return
    if len(result_list)==2:
        result_list[0] = result_list[0] + result_list[1]
        return 
    else:
        add(result_list)
    
for tc in range(1,T+1):
    K = int(input())
    arr = list(map(int,input().split()))

    add(arr)
