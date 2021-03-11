import sys
sys.stdin = open('input.txt')

T = int(input())
operater = ['+','-','*','/']

def Oper(x,y,op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y  
    elif op == '*':
        return x*y
    elif op == '/':
        return int(x/y)

def Cal(op,count,result):
    global max_value
    global min_value

    for i in range(4):
        if op[i] != 0:
            op[i] -= 1
            temp = Oper(result,numbers[count+1],operater[i])
            Cal(op,count+1,temp)
            op[i] += 1
    
    if count == N-1:
        max_value = max(max_value,result)
        min_value = min(min_value,result)

for tc in range(1,T+1):
    max_value = -100000000
    min_value = 100000000

    N = int(input())
    op = list(map(int,input().split()))
    numbers = list(map(int,input().split()))

    result = numbers[0]
    Cal(op,0,result)

    print("#{} {}".format(tc, max_value - min_value))