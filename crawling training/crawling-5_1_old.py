# import package
from bs4 import BeautifulSoup
import requests
import urllib
import re
import pandas as pd
from newspaper import Article
from selenium import webdriver

keyword = '아마존닷컴'
page_num = 0  # 0, 10, 20...
news_df = pd.DataFrame()

# selenium headless mode
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)


while 1:
    # google news crawling
    url = f'https://www.google.com/search?q={keyword}&sca_esv=1814fa2a4600643d&tbas=0&tbs=qdr:m&tbm=nws&ei=rE3pZeLxNeHX1e8PpdOcMA&start={page_num}&sa=N&ved=2ahUKEwji9-zrsuGEAxXha_UHHaUpBwYQ8tMDegQIBBAE&biw=2560&bih=1313&dpr=1'
    req = requests.get(url)
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')

    # last page check
    if soup.select('div.BNeawe.vvjwJb') == []: break

    title_list = [t.text for t in soup.select('div.BNeawe.vvjwJb')]  # title
    
    url_list = []

    # url
    for u in soup.select('a'):
        for t in title_list:
            if t in u.text:
                temp_url = urllib.parse.unquote(u['href'])
                temp_url = re.findall("http\S+",temp_url)[0][:-3]
                url_list.append(temp_url)

    # article
    for ind, news_url in enumerate(url_list):
        try:
            article = Article(url=news_url)
            article.download()
            article.parse()    
            news_article = article.text
        except:  # ssl error
            driver.get(news_url)
            article.download(input_html=driver.page_source)
            article.parse()
            news_article = article.text

       
        news_df = pd.concat([news_df, pd.DataFrame([[title_list[ind], news_article, news_url]])])

    news_df[0] = news_df[0].apply(lambda x: re.sub('\s+',' ',x))    
    news_df = news_df.reset_index(drop=True)

    #page_num += 10
    news_df.to_excel('news_crawling.xlsx', index=False)

news_df.columns = ['제목','본문','URL']

