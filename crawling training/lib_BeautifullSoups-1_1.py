#[BeautifunSoup] 파이썬으로 구글 뉴스 크롤링해보기

# import 패키지
from bs4 import BeautifulSoup
import requests
import urllib
import re
import pandas as pd
from newspaper import Article
from selenium import webdriver


keyword = '파이썬 기초'
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

title_list = [t.text for t in soup.select('div.ilUpNd.UFvD1.aSRlid')] #title

url_list = []

#print(soup.prettify())
#print(soup.select('div.ilUpNd.UFvD1.aSRlid'))
#print(title_lsit)
#print(url)


# url
for u in soup.select('a'):
    i = 0
    i+= 1
    for t in title_list:            
        if t in u.text:
            temp_url = urllib.parse.unquote(u['href'])
            temp_url = re.findall(r"http\S+",temp_url)[0][:-3]
            url_list.append(temp_url)
            print("t_" + str(i) + " : " + temp_url)

print("title_list_len : " + str(len(title_list)))
print("url_list_len : " + str(len(url_list)))

# article
for ind, news_url in enumerate(url_list):
    try:
        article = Article(url=news_url)
        article.download()
        article.parse()    
        news_article = article.text
    except: #ssl error
        driver.get(news_url)
        article.download(input_html=driver.page_source)
        article.parse()
        news_article = article.text

'''

    if ind < len(title_list):
        news_df = pd.concat([news_df, pd.DataFrame([[title_list[ind], news_article, news_url]])])

news_df[0] = news_df[0].apply(lambda x: re.sub(r'\s+',' ',x))
news_df = news_df.reset_index(drop=True)

#page_num += 10
if not news_df.empty:
    news_df.to_excel('news_crawling.xlsx', index=False)
else:
    print("news_df가 비어 있습니다. 데이터를 확인하세요.")

news_df.columns = ['제목','본문','URL']

'''

# WebDriver 종료
driver.quit()