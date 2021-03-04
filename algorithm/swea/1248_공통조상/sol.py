import sys
sys.stdin = open("input.txt","r")

T = int(input())

for tc in range(1,T+1):
    V, E ,n1 ,n2 = list(map(int,input().split()))

    point = [0] * (V+1)
    point2 = [[0] for _ in range(V+1)]

    tree_list = list(map(int,input().split()))

    for i in range(0,len(tree_list),2):
        point[tree_list[i+1]] = (tree_list[i])
        point2[tree_list[i]].append(tree_list[i+1])
    
    n1_list = []
    n2_list = []
    
    while True:
        n1_list.append(point[n1])
        n2_list.append(point[n2])

        n1 = point[n1]
        n2 = point[n2]

        if n1 == 0 and n2 == 0:
            break

    result = 0

    for i in n1_list:
        for j in n2_list:
            if i == j:
                result = i
                break
        if result != 0:
            break

    stack = [result]
    count = 1

    while stack:
        now = stack.pop()
        for i in range(1,len(point2[now])):
            stack.append(point2[now][i])
            count += 1

    print("#{} {} {}".format(tc,result,count))





