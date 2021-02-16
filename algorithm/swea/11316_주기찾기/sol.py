import sys
sys.stdin = open("input.txt")

T = int(input())

# def PG(A,s,p,q,m):
#     value = (s*p+q)%m
#     if value in A:
#         return value
#     else:
#         A.append(value)
#         PG(A,value,p,q,m)


# for tc in range(1, T+1):
#     s,p,q,m = map(int,input().split())
#     A = [s]
#     result = PG(A,s,p,q,m)



# for tc in range(1, T+1):
#     s,p,q,m = map(int,input().split())
#     A = [s]
#
#     value = (s*p+q)%m
#
#     while True:
#         if value in A:
#             break
#         else:
#             A.append(value)
#             value = (value*p+q)%m
#
#     for i in range(len(A)):
#         if A[i] == value:
#             result = len(A)-i
#             break
#
#     print("#{} {}".format(tc,result))

for tc in range(1, T+1):
    s,p,q,m = map(int,input().split())
    A = [s]
    counting = [0] * 1000000

    value = s
    result = 0

    while True:
        value = (value*p+q)%m
        counting[value] += 1
        if counting[value] == 2:
            result += 1
        if counting[value] == 3:
            break

    print("#{} {}".format(tc,result))