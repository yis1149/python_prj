# url 제공후 chatgpt로 크롤링 소스 생성요청
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# 크롬 드라이버 옵션 설정
options = Options()
options.add_argument('--headless')  # 브라우저 안 띄우기
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 크롬 드라이버 경로
#driver_path = '/path/to/chromedriver'  # 크롬 드라이버 경로로 변경

# 스크래핑할 상품 URL
url = 'https://www.coupang.com/vp/products/7666070794?itemId=23361506529&vendorItemId=86478559145'

# 웹드라이버 실행
#driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(3)

# 리뷰 탭으로 이동
try:
    review_tab = driver.find_element(By.XPATH, "//a[@data-tab-section='productReview']")
    review_tab.click()
    time.sleep(3)
except:
    print("리뷰 탭을 찾을 수 없습니다.")
    driver.quit()
    exit()

# 스크롤 또는 다음 페이지 탐색을 통한 리뷰 수집
reviews = []
page = 1
while page <= 5:  # 원하는 만큼 페이지 수 조절 가능
    print(f"{page}페이지 수집 중...")
    time.sleep(2)
    review_elements = driver.find_elements(By.CLASS_NAME, 'sdp-review__article__list__headline')

    for element in review_elements:
        try:
            content = element.text.strip()
            if content:
                reviews.append(content)
        except:
            continue

    try:
        next_button = driver.find_element(By.CLASS_NAME, 'btn-next')
        if 'disabled' in next_button.get_attribute('class'):
            break
        next_button.click()
        page += 1
    except:
        print("다음 페이지 버튼 없음")
        break

driver.quit()

# 데이터 저장
df = pd.DataFrame({'Review': reviews})
df.to_csv('coupang_reviews.csv', index=False, encoding='utf-8-sig')

print("완료! coupang_reviews.csv 파일로 저장되었습니다.")