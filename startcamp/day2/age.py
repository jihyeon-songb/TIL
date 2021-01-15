import requests

name = 'jihyeon'
#API 요청 url 확인 + 필요한 데이터 건네주기 
url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json()

name = response['name']
age = response['age']
print(f'{name}님의 예상 나이는 {age}살 입니다.')

#https://api.nationalize.io/?name=jihyeon 이름 쓰면 나라 맞추기