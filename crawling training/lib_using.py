import requests
from bs4 import BeautifulSoup
from newspaper import Article # 패키지 불러오기

link = 'https://view.asiae.co.kr/article/2023032217473512545?utm_source=newsstand.naver.com&utm_medium=referral&utm_campaign=top6'




response = requests.get("https://xn--sh1bx7bj4cm6h09ezw0a.com/")
html = response.text

soup = BeautifulSoup(html, "html.parser")

items = soup.select_one(".depth0 gnb_menu0")





print(items)
