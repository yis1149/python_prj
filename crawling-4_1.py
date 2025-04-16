
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import subprocess

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

#try:
driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option, enable_cdp_events=True, incognito=True)
#except:
#    chromedriver_autoinstaller.install(True)
#    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

driver.implicitly_wait(5)

# 검색 입력창 찾기
search_box = driver.find_element(By.NAME, 'input')
search_box.send_keys('파이썬')	

# 검색어 실행
search_box.submit()

