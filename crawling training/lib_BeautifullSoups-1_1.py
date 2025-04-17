#[BeautifunSoup] 파이썬으로 구글 뉴스 크롤링해보기

# import 패키지
from bs4 import BeautifulSoup
import requests
import urllib
import re
import pandas as pd
from newspaper import Article
from selenium import webdriver


keyword = '아마존닷컴'
page_num = 0 #0, 10,20...
news_df = pd.DataFrame()

#selenium headless mode
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

'''
# google news crewling
url = f'https://www.google.com/search?q={keyword}&sca_esv=1814fa2a4600643d&tbas=0&tbs=qdr:m&tbm=nws&ei=rE3pZeLxNeHX1e8PpdOcMA&start={page_num}&sa=N&ved=2ahUKEwji9-zrsuGEAxXha_UHHaUpBwYQ8tMDegQIBBAE&biw=2560&bih=1313&dpr=1'
req = requests.get(url)
content = req.content
soup = BeautifulSoup(content, 'html.parser')

#title_list = [t.text for t in soup.select('div.dURPMd')]  # title

#print(soup.prettify())
print(soup.select('a')[0].text)
'''


#while 1:

# google news crawling
url = f'https://www.google.com/search?q={keyword}&newwindow=1&sca_esv=1814fa2a4600643d&tbas=0&tbs=qdr:m&tbm=nws&ei=rE3pZeLxNeHX1e8PpdOcMA&start={page_num}&sa=N&ved=2ahUKEwji9-zrsuGEAxXha_UHHaUpBwYQ8tMDegQIBBAE&biw=2560&bih=1313&dpr=1'
req = requests.get(url)
content = req.content
soup = BeautifulSoup(content, 'html.parser')

# last page check
#if soup.select('div.ilUpNd.UFvD1.aSRlid') == []: break

title_lsit = [t.text for t in soup.select('div.ilUpNd.UFvD1.aSRlid')] #title

url_list = []

print(soup.prettify())
print(soup.select('div.ilUpNd.UFvD1.aSRlid'))
print(title_lsit)


# url
for u in soup.select('a'):
    for t in title_lsit:
        print(t.text)
        if t in u.text:
            #temp_url = urllib.parse.unquote(u['href'])
            #temp_url = re.findall("http\S+",temp_url)[0][:-3]
            #url_list.append(temp_url)
            print(u.text)
