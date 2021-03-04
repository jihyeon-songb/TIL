## 1861_정사각형 방

N^2개의 방이 NXN 형태로 늘어서있다. i번쨰 줄 왼쪽에서 j번쨰 방에는 1이상 N^2이하의 수 A가 적혀있으며 이 숫자는 모든 방에 대해 다르다. 

당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다. 물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야한다. 

처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라

**[입력]**

테스트 케이스의 첫 번째 줄에는 하나의 정수 N이 주어진다.

다음 N개의 줄에는 A가 공백 하나로 구분되어 주어진다.

**[출력]**

처음 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다.

이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중 적힌 수가 가장 작은 것을 출력한다.



### ✔ 코드 풀이

첫 시작만 찾아서 이동하면 되겠다고 생각이 들었다.

첫 시작인 아닌 값은 주변에 자신-1. 자신+1 이 두개 다 있거나 자신-1인 값이 있는 것이다.

이 값만 제외할 수 있는 함수를 만들었다.

자신-1 ,자신+1이 둘 다 있는 것은 count == 2가 되는 것이고

자신-1만 있는 것은 check == 0이 되는 것이다.

이 값인 것은 False로 리턴하여 연산이 되지 않게 하였다.

```python
def Pass(i,j):
    count = 0
    check = 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
        if arr[nx][ny] == arr[i][j] - 1:
            count += 1
            check = 0
        elif arr[nx][ny] == arr[i][j] + 1:
            count += 1
    # 주변에 자신보다 1큰 값, 1작은 값 둘다 있는 값과 
    # 1큰 값만 있는 것은 False
    if count == 2 or check == 0:
        return False
    # 주변에 자신보다 1큰 값만 있거나 1큰 값. 1작은 값 둘다 없는 값만 True 
    else:
        return True
```

그 다음으로는 방을 이동시켰다. 

하나씩 deque에 넣어서 deque의 값이 없어질 때까지 while문을 돌게하면

방을 이동하고 count로 몇번 이동했는지 세어준다.

다 돌고나면 리스트로 시작점의 값과 count를 리스트로 값을 넘겨준다.

```python
# 첫 시작부터 끝까지 움직이기
def Move(i,j,visited):
    dq = deque()
    dq.append((i,j))
    visited[i][j] = 1
    count = 1
    while dq:
        x,y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:continue
            if arr[nx][ny] == arr[x][y] + 1:
                dq.append((nx,ny))
                count += 1
                visited[nx][ny] = 1
    
    return [arr[i][j],count]
```

넘겨온 값을 받아서 방을 제일 많이 이동한 횟수를 찾아줘 max_move에 저장하고

시작점의 값은 start_idx에 저장한다. 

최대가 여럿이면 시작점의 값은 제일 작은 값으로 저장해야하기 때문에 

최대가 같을때라는 elif문을 따로 주어서 더 작은 것을 찾아준다. 

```python
max_move = 0
start_idx = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            # 첫 시작점이 맞다면
            if Pass(i,j):
                start, count = Move(i,j,visited)
                if max_move < count:
                    start_idx = start
                    max_move = count
                elif max_move == count:
                    if start_idx > start:
                        start_idx = start
```

😀 처음에 생각했던대로 구현했는데 답이 잘 나와서 만족스럽다! 굉장히 재미있는 문제였다!!

​	 deque를 사용했는데 이 부분에서 다른 것을 사용해서 구현할 수 있는지 생각해봐야겠다.

