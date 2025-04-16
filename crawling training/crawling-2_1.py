# 동적 웹크롤링 - selenium 기초 사용법

# selenium 의 webdriver 를 사용하기 위한 import
from selenium import webdriver

# selenium 으로 로케이터 사용을 위한 import
from selenium.webdriver.common.by import By

# selenium 으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys

# selenium 으로 chrome option  조작하기 위한 import
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

# 해당 부분 사용하기 위해서는 먼저 pip install webdriver_manager 선행 되어야함.
# chrome 자동 닫힘 해결을 위해 추가 했지만 options 만 적용하여도 됨 
from webdriver_manager.chrome import ChromeDriverManager  

# 페이지 로딩을 기다리는데 사용할 time 모듈 import
import time


# chrome 실행후 자동으로 창이 닫히는 문제 해결을 위한 option 적용
options = Options()
options.add_experimental_option("detach", True)

# 크롬드라이버 실행
#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


# 크롬드라이버 url 주소 넣고 실행
driver.get('https://www.google.co.kr')

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(5)

# 검색어 창을 찾아 search 변수에 저장 (By.CLASS_NAME 방식)
search_box = driver.find_element(By.CLASS_NAME, "gLFyf")		

# 검색 버튼을 찾아 search 변수에 저장
#search_button = driver.find_element(By.CLASS_NAME, "gNO89b")	
#search_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')	

# 검색어 창을 찾아 search 변수에 저장 (By.XPATH 방식) (※ html 코드 위에서 마우스 우클릭-> copy -> Copy Xpath)
#search_box = driver.find_element_by_xpath('//*[@id="APjFqb"]')


# 검색어 입력창에 '파이썬' 검색어 입력후 '엔터키' 입력
search_box.send_keys('파이썬')	
time.sleep(1)
search_box.send_keys(Keys.RETURN)

# click 함수는 ()안에 아무것도 넣지 않으면 좌클릭을 수행
#search_button.click()

#time.sleep(1)