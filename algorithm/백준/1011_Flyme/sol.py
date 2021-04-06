import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    s, e = map(int,input().split())
    count = e-s

    result = 0
    total = 0
    i = 0
    while True:
        i += 1
        total += (2*i)
        if total >= count:
            result = i*2
            if total-i >= count:
                result -= 1
            break

    print(result)