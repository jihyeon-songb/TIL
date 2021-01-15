import requests
import pprint

# API 요청 & 응답
# .text -> 데이터를 꺼낸다.
# json() -> 메서드(기능)을 실행시킨다.
name = 'ruby'

# 쿼리 스트링. 파라미터..
# API 요청 url 확인한다 (필요한 데이터 넘겨주기)
url = f'https://api.nationalize.io/?name={name}'

# 요청 보내기
response = requests.get(url).json()
print(type(response)) # .text으로 받으면 타입이 str로 됨 dict으로 되어야함(json사용)

# 응답 결과 확인 후 정보 추출하기
pprint.pprint(response)
name = response['name']
country = response['country'][0]['country_id']
p = round(response['country'][0]['probability']*100,2)


print(f'{name}의 국적은 {p}% 확률로 {country}입니다.')