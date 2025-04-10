# 정적 웹크롤링 - request / beautifulsoup

# requests 패키지 가져오기
import requests

# 가져올 url 문자열로 입력
url = 'https://www.naver.com'

# requests의 get 함수를 이용해 해당 url로 부터 html이 담긴 자료를 받음
response = requests.get(url)

# 받아온 html 을 변수에 담음
html_text = response.text

# BeautifulSoup 패키지 불러오기
from bs4 import BeautifulSoup as bs

# html을 정리된 형태로 변환
html = bs(html_text, 'html.parser')

print(html)
