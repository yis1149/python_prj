# import package
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True) # chrome 실행후 자동으로 창이 닫히는 문제 해결을 위한 option 적용

# 크롬드라이버 실행
driver = webdriver.Chrome(options=options)

# 크롬드라이버 url 실행


# 1. 콩볶는사람들 Start
driver.get('https://www.xn--sh1bx7bj4cm6h09ezw0a.com/member/login.php')
time.sleep(3) #페이지 로딩 대기

# login Id 입력창 찾기
loginId = driver.find_element(By.ID, "loginId")
# login Pass 입력창 찾기
loginPw = driver.find_element(By.ID, "loginPwd")
# login Id 입력창에 ID 입력
loginId.send_keys('yis1149')
# login Pass 입력창에 pass 입력
loginPw.send_keys('sando1025!')
loginPw.send_keys(Keys.ENTER)
time.sleep(3) #페이지 로딩 대기

# 출석체크 팝업 찾기
driver.find_element(By.CLASS_NAME, "sys_pop").click()
time.sleep(3) #페이지 로딩 대기

# 출석체크 버튼 찾기
driver.find_element(By.CLASS_NAME, "btn_attend_check").click()
time.sleep(3) #페이지 로딩 대기

# Webdriver 종료
driver.quit()


# 2. illycaffe Start
driver = webdriver.Chrome(options=options)
driver.get('https://shop.illycaffe.co.kr/member/login.php')
time.sleep(3)

# login Id 입력창 찾기
loginId = driver.find_element(By.ID, "loginId")
# login Pass 입력창 찾기
loginPw = driver.find_element(By.ID, "loginPwd")
# login Id 입력창에 ID 입력
loginId.send_keys('yis1149')
# login Pass 입력창에 pass 입력
loginPw.send_keys('faceme1025!')
loginPw.send_keys(Keys.ENTER)
time.sleep(3) #페이지 로딩 대기

#  출석체크 이벤트 페이지로 이동(2025.04.18 Url)
driver.get('https://shop.illycaffe.co.kr/event/attend_stamp.php?sno=28')
time.sleep(3) #페이지 로딩 대기

# 출석체크 버튼 찾기
driver.find_element(By.CLASS_NAME, "btn_attend_check").click()
time.sleep(3) #페이지 로딩 대기

# Webdriver 종료
driver.quit()

