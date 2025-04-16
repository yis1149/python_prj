import time
import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By




options = uc.ChromeOptions()

# 크롬드라이버 생성
driver = uc.Chrome(options=options, enable_cdp_events=True, incognito=True)

# Google 접속
driver.get("https://www.google.com")

# 검색 입력창 찾기
#search_box = driver.find_element(By.NAME, 'q')
search_box = driver.find_element(By.CLASS_NAME, "gLFyf")		

# 검색어 입력
search_box.send_keys('파이썬')

# 검색어 실행
search_box.submit()
time.sleep(5)

