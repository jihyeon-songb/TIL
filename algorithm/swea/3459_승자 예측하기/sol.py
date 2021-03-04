import sys
sys.stdin = open("input.txt","r")

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    x = 9
    sum_value = 8
    result = 'Bob'
    start = 1

    while True:
        if N == 1:
            break

        mid = (start+x)//2

        if start < N <= mid:
            result = "Alice"
            break
        
        if mid < N <= x:
            result = "Bob"
            break

        sum_value *= 4
        start = x
        x += sum_value

    
    print("#{} {}".format(tc,result))


            


                