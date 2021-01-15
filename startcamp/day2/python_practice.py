# 1. 기초자료형
number = 3
# print(number)
# print(type(number)) #자료형 확인
string = '문자열' 
# print(string)
# print(type(string))
boolean = True # Boolean
# print(boolean)
# print(type(boolean))

string_number = '3' # 형 변환
# print(int(string_number)+5)

# 2. f-string (string interpolation)
name = '송지현'
# print('제 이름은 ' + name + '입니다.')
# print(f'제 이름은 {name}입니다.')

# 3. List
my_list = ['python', 'html', 'markdown',] #리스트 마지막에 트렐리 콤마, 찍기
# print(my_list[2])
my_list[2] = 'java'
# print(my_list[2],my_list)

# 4. Dictionary
age_dict = {
    '박소현' : 25, 
    '김지용' : 63,
}
# 딕셔너리 요소(원소) 접근
# print(age_dict['김지용'])
# print(age_dict['박소현'])
# print(age_dict.get('김지용'))

# 딕셔너리 요소 변경
age_dict['김지용'] = 103
# print(age_dict['김지용'])

# 기초 연산자
# 산술 연산자
# print(3 + 5)
# print(3 - 5)
# print(3* 5)
# print(100/5) #나누기
# print(100//7) #몫
# print(100%7) #나머지
# print(2**5) #제곱
# #비교 연산자
# print(5==5)
# print(5=='3')
# print(5!=3)
# print(5>=3)
# print(5<3)

#조건문
n=11
#1. 주어진 양수 n이 홀수, 짝수인지 판단하여 출력하는 코드를 작성해라
# if n % 2 == 1:
#     print('홀')
# else:
#     print('짝')

# 2. 주어진 숫자 n이 양수인지, 0인지, 음수인지 판단하여 출력하는 코드

# 반복문
# numbers = [1,2,3]
# for number in numbers:
#     print(number)

numbers = range(1,10)
for number in numbers:
    print(number)

# 숫자 뭐시기는 홀수입니다.
for number in numbers:
    if number % 2 == 1:
        print(f'{number}는 홀수입니다.')
    else:
        print(f'{number}는 짝수입니다.')
