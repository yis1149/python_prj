#사용자가 입력한 url에서 text를 크롤링 해주는 패키지 import
from newspaper import Article
#크롤링할 url 주소
url = 'http://www.hani.co.kr/arti/society/health/986131.html'

#한국어이므로 language='ko'
article = Article(url, language='ko')
article.download()
article.parse()