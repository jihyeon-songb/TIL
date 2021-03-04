import sys
from collections import deque
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):
    # 데이터의 길이, 연락의 시작점 입력
    length, start = map(int,input().split())
    # {from, to, from. to... }
    from_to = list(map(int,input().split()))

    # 0~100번의 인덱스를 가진 빈 배열 생성
    arr = [[0] for _ in range(101)]
    # from인덱스에 to의 값을 넣어준다
    for i in range(0,len(from_to),2):
        arr[from_to[i]].append(from_to[i+1])

    # deque 만들기
    dq = deque()
    # 처음에 시작점과 첫번째로 방문함을 넣어줌
    dq.append((start,1))
    # 0~100번을 방문했는지 체크해 줄 리스트
    visited = [0] * 101
    # 시작점 
    visited[start] = 1

    while dq:
        x, o = dq.popleft()
        for i in range(1,len(arr[x])):
            nx = arr[x][i]
            if visited[nx] == 0:
                visited[nx] = o+1
                dq.append((nx,o+1))
                

    last = 0
    last_max = 0
    for i in range(101):
        if visited[i] > 0:
            if last <= visited[i]:
                last_max = i
                last = visited[i]

    print('#{} {}'.format(tc,last_max))


    

        

