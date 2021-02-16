## 11316_주기찾기

> 슈도랜덤 제너레이터의 주기를 구하는 프로그램을 작성하라.

- Ai = s (i = 0)
- Ai = (p*Ai-1+q) mod m (i>=1)

슈도랜덤 제너레이터의 주기란, 어떤 정수 n0이상인 모든 n에 대해 An+p = An 을 만족하는 가장 작은 자연수 p를 말한다. 예를 들어, A = [6, 8, 3, 7, 2, 3, 7, 2, 3, 7, 2,...]처럼 만들어지고 [3, 7, 2]가 계속 반복된다면 2이상의 모든 정수 n에 대해 An+3 = An이므로, 주기는 3이다.

**[입력]**

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 네정수 s,p,q,m(0 <= s,p,q < m <= 10**6)

이 공백 하나로 구분되어 주어진다.

### 코드 풀이

### 1

```python
def PG(A,s,p,q,m):
    value = (s*p+q)%m
    if value in A:
        return value
    else:
        A.append(value)
        PG(A,value,p,q,m)
```

처음에는 재귀로 풀어보려고했다.

하지만 재귀깊이가 너무 깊다는 에러가 나왔다..

### 2

```python
 while True:
        if value in A:
            break
        else:
            A.append(value)
            value = (value*p+q)%m

    for i in range(len(A)):
        if A[i] == value:
            result = len(A)-i
            break
```

두 번째로는 while문을 이용해 풀어보려했다.

while문을 이용해 계속 A_value를 계산하고 list안에 A_value와 같은 값이 있다면 break를 해주어 반복을

멈추게했다.

그리고 A_list를 순회하여 멈추게 했던 value와 같은 값의 인덱스를 구했고 

그 값을 A_list의 길이에서 빼주어서 반복이 되는 주기를 찾았다.

하지만 이것도 시간초과가 나왔다.. m이 클 때 값이 나오는데 굉장히 오래걸렸다.

 ### 3

```python
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
```

세 번째로는 카운팅 정렬를 이용하여 풀었다.

mod m을 하기 때문에 값이 다 m보다 클 수는 없다.

그래서 m의 최대인 10^6의 갯수의 카운팅 리스트를 만들었다.

그리고 while문으로 돌려서 그 value인덱스에 1을 더해주고

만약 값이 2가 되면 그 인덱스부터는 주기가 생기는 것이기때문에 결과값에 카운팅 해준다.

그리고 3이 되면 다시 주기가 되돌아온것이기때문에 반복문에서 나가고 결과값을 출력해준다.

이것도 시간이 나름 오래 걸린다..

위에 있는 코드가 20000ms정도 걸렸다면 이 코드는 14000ms정도 걸린다.

시간초과는 나지않아 통과하였지만 조금 더 빠른 코드를 생각해봐야겠다.

