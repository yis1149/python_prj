# 정적 웹크롤링 - request / beautifulsoup
# 정적 웹크롤링 - 텍스트, 하이퍼링크, 이미지 가져오기

# Step 1. 필요한 패키지 불러오기
from bs4 import BeautifulSoup as bs

import requests


# Step 2. 검색 키워드 입력
query = input('검색 키워드 입력 : ')


# Step 3. 입력 키워드를 포함한 Url 주소 생성
url = 'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=' + '%s'%query


# Step 4. requests 패키지를 이용해 url 의 html 가져오기
response = requests.get(url)
html_text = response.text


# Step 5. beautifullsoup 패키지고 파싱 후 soup 에 저장
soup = bs(response.text, 'html.parser')


# Step 6. 타겟 텍스트 추출 (뉴스 제목 텍스트)
news_titles = soup.select("a.news_tit")

for i in news_titles:
    title = i.get_text()
    print(title)


# Step 7. 타겟 하이퍼링크 추출
for j in news_titles:
    href = j.attrs['href']
    print(href)

# Step 8. 타겟 썸네일 이미지 추출
news_content_div = soup.select(".news_contents")
news_thumbnail = [thumbnail.select_one(".thumb") for thumbnail in news_content_div]

link_thumbnail = []

for img in news_thumbnail:
    if img is not None and 'data-lazysrc' in img.attrs:
        link_thumbnail.append(img.attrs['data-lazysrc'])

# 이미지 저장 폴더 생성
import os

# path_folder 경로 지정
path_folder = '/python_prj/img_download/'

if not os.path.isdir(path_folder):
    os.mkdir(path_folder)

# 이미지 다운로드
from urllib.request import urlretrieve

img_idx = 0

for link in link_thumbnail:
    img_idx += 1
    urlretrieve(link, path_folder + f'{img_idx}.jpg')