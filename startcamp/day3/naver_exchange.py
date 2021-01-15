import requests
from bs4 import BeautifulSoup

# 웹페이지 크롤링
# 크롤링 할 때 필요한 기능(라이브러리) 가져오기 import.
# beautifulSoup 데이터를 구조화(예쁘게) 만들어 준다.

# 데이터를 추출할 url 확인
url = 'https://finance.naver.com/marketindex/'

# 요청 보내기
# response = requests.get(url)
# print(response) -> Reponse 200 응답이 잘 왔다.
response = requests.get(url).text # 어마어마하게 긴 문자열 

# 응답받은 값을 추출하기 쉬운 형태로 구조화(예쁘게 만들기)
soup = BeautifulSoup(response,'html.parser') # 자료형은 거대한 문자열이지만 html파싱해야함.

# 원하는 데이터 추출하기
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print(f'현재 원/달러 환율은 {exchange}입니다.')