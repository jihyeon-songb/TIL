import sys
sys.stdin = open('input.txt')

T = int(input())

def swim(month,cost):
    global result

    if month >= 12:
        if result > cost:
            result = cost
        return

    if plan[month] != 0:                                                                                                                                                                                          
        swim(month+1,cost+plan[month]*d)
        swim(month+1,cost+m)
        swim(month+3,cost+t_m)
    else:
        swim(month+1,cost)
    

for tc in range(1,T+1):
    d, m, t_m, y = map(int,input().split())
    plan = list(map(int,input().split()))

    result = y
    
    swim(0,0)

    print("#{} {}".format(tc,result))
