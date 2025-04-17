#파이썬으로 뉴스 데이터를 크롤링을 할 수 있는 Newspaper 패키지
# pip install newspaper3k
# newspaper import 에러시 pip install lxml_html_clean 추가 설치 필요
from newspaper import Article # 패키지 불러오기

# 뉴스 기사 URL
link = 'https://view.asiae.co.kr/article/2023032217473512545?utm_source=newsstand.naver.com&utm_medium=referral&utm_campaign=top6' 
# URL 과 언어를 입력
article = Article(link, language='ko')

article.download()
article.parse()
title = article.title
text = article.text
date = article.publish_date


print('title = ' + title)
print('text = ' + text[:100])
print(date)
