N = int(input())

check = False
for i in range(1,N+1):
    total = 0 
    num = i
    while num:
        total += num%10
        num //= 10

    if i + total == N:
        check = True
        break

if check:
    print(i)
else:
    print(0)
        