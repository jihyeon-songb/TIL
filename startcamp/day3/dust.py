# 공공 데이터 API 활용 실습
# 1. 필요한 라이브러리 import 하기 
import requests
import pprint

# 2.API URL 및 KEY값 확인
key = 'urbmhj6RqcNKYhTdWScvQ%2B4QCMFrIYQJuo9h6ZA2xBiCuHRMYVcPYiXkRvdvb2w9beTWqZBKurlc7ymQ9qjPSA%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName=광주&returnType=json'

# url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=urbmhj6RqcNKYhTdWScvQ%2B4QCMFrIYQJuo9h6ZA2xBiCuHRMYVcPYiXkRvdvb2w9beTWqZBKurlc7ymQ9qjPSA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.0'

# 3. 요청 및 응답값 확인
response = requests.get(url).json()
# pprint.pprint(response)

# 최종 출력 문자열
pm_value = response['response']['body']['items'][4]['pm10Value']
sido_name = response['response']['body']['items'][4]['sidoName']
station_name = response['response']['body']['items'][4]['stationName']

# print(f'{sido_name}의 미세먼지 농도는 {pm_value}입니다. (측정소: {station_name})')

# 5. 텔레그램 메시지 전송
token = ''
api_url = f'https://api.telegram.org/bot{token}'

chat_id = ''

text = f'{sido_name}의 미세먼지 농도는 {pm_value}입니다. (측정소: {station_name})'
send_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(send_url)